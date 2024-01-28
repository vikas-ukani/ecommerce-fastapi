from fastapi import APIRouter
from app.db import Category, serializeList

router = APIRouter()


@router.get("/get-categories")
async def all_categories():
    return serializeList(Category.find({}))
