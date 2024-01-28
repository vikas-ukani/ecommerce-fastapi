from app.db import serializeDict, User
from bson.objectid import ObjectId


async def get_users() -> list:
    users = []
    async for user in User.find():
        del user["password"]
        if "password_confirm" in user:
            del user["password_confirm"]
        users.append(serializeDict(user))
    return users


async def create_user(user: dict) -> dict:
    user = User.insert_one(user)
    newUser = User.find_one({"_id": user.inserted_id})
    return serializeDict(newUser)


async def get_user_by_email(email: str):
    print("Fine user by email: " + email)
    user = await User.find_one({"email": email})
    return serializeDict(user) if user is not None else None


async def get_user(id: str) -> dict:
    newUser = await User.find_one({"_id": ObjectId(id)})
    return serializeDict(newUser)


async def update_user(id: str, param: dict):
    if len(param) < 1:
        return False
    user = await User.find_one_and_update({"_id": ObjectId(id)}, {"$set": param})
    return True if user is not None else False


async def delete_user(id: str):
    user = User.find_one({"_id": ObjectId(id)})
    if user:
        await User.delete_one({"_id": ObjectId(id)})
        return True
    return False
