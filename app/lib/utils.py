from bson import ObjectId
from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from fastapi import Depends, HTTPException, status
from app.config.settings import settings
from app.db import User
from app.db import serializeDict
from app.middleware.log_middleware import logger

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
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return jwt_token


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        decoded = jwt.decode(token, key=settings.JWT_SECRET_KEY,
                             algorithms=settings.JWT_ALGORITHM)
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
        logger.info(error.__str__())
        raise HTTPException(status_code=440, detail="Token has been expired")
