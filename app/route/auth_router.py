import datetime
from fastapi import APIRouter, status,  HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from app.schema.auth_schema import LoginSchema, SignUpSchema
from app.db import serializeDict, User
from app.lib.utils import (
    create_token,
    get_current_user,
    hash_password,
    verify_password,
)
from app.schema.user_schema import UserBaseSchema
from app.log_manager import logger

router = APIRouter()


@router.post("/signin", status_code=status.HTTP_200_OK)
async def signIn(data: LoginSchema):
    user = serializeDict(User.find_one({"email": data.email}))

    if user:
        del user['password']
        del user['password_confirm']
        if not data.password and not verify_password(data.password, user["password"]):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Invalid login credentials. Try again.")
        return {"success": True, 'user': user, "token": create_token(str(user["_id"]))}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password.",
        )


@router.get(
    "/me",
    response_model=UserBaseSchema,
    # response_model_exclude_unset=True,
    summary="Get User by token",
)
async def get_me(user=Depends(get_current_user)):
    return user


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(input: SignUpSchema):
    existingUser = User.find_one({"email": input.email})
    if existingUser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The email is already exists.",
        )
    if input.password != input.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password not matching with confirm password.",
        )

    has_password = hash_password(input.password)
    del input.password
    del input.confirm_password
    input.password = has_password
    input.created_at = datetime.datetime.utcnow()
    input.updated_at = input.created_at

    try:
        user = User.insert_one(jsonable_encoder(input))
        logger.info(user)
        User.find_one({"_id": user.inserted_id})
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Internal server error found.",
        )
    return {
        "success": True,
        "token": create_token(str(user.inserted_id)),
        "message": "Your account has been created.",
    }
