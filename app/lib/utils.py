from bson import ObjectId
from decouple import config
from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from fastapi import Depends, HTTPException, status
from app.db import User
from app.db import serializeDict


pwd_context = CryptContext(schemes=["bcrypt"])
security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/signin")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def create_token(user_id):
    to_encode = {"user_id": user_id}
    jwt_token = jwt.encode(
        to_encode, config("JWT_SECRET_KEY"), algorithm=config("JWT_ALGORITHM")
    )
    return jwt_token


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded = jwt.decode(token, key=config("JWT_SECRET_KEY"), algorithms=config("JWT_ALGORITHM"))
        user_id = decoded.get("user_id")
        user = User.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return serializeDict(user)
    except Exception as error:
        print(error)
        raise HTTPException(status_code=440, detail="Token has been expired")
    
