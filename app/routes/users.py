from fastapi import APIRouter, Body
from ..models.user_helper import (
    get_user,
    create_user,
    get_users,
    delete_user,
    update_user,
)
from ..schemas.user import CreateUserSchema
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/get-users", response_description="Get all users from database.")
async def getUsers():
    return await get_users()


@router.post("/create-users", response_description="Create new user into database.")
async def createUsers(param: CreateUserSchema = Body()):
    user = jsonable_encoder(param)
    newUser = await create_user(user=user)
    return {"data": newUser, "message": "User has been created."}
