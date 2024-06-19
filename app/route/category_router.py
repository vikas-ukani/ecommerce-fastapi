from fastapi import APIRouter
from app.helper.category_helper import fetch_categories
from app.schema.category_schema import CategoryModel
from typing import List

router = APIRouter()


@router.get("/get-categories", response_model=List[CategoryModel], response_description="All Categories")
async def all_categories():
    return await fetch_categories()
