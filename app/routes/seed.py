from fastapi import APIRouter
from app.seed.products_seed import seed_products_data
from app.seed.categories_seed import seed_categories_data

router = APIRouter()


@router.get("/seed/products", tags=["Seed"])
async def seed_products():
    await seed_products_data()
    return {"message": "Products has been seeded"}


@router.get("/seed/categories", tags=["Seed"])
async def seed_categories():
    await seed_categories_data()
    return {"message": "Categories has been seeded"}
