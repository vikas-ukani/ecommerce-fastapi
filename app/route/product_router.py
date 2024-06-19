from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.product_schema import ProductFilterModel, ProductResponseModel, ProductBaseModel
import re
from app.helper.product_helper import product_by_filter, getProductById
from app.log_manager import logger

router = APIRouter()


@router.get("/product/{id}", response_model=ProductBaseModel, response_description="Get product by id")
async def get_product(id: str):
    product = getProductById(id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid product id.",
    )


@router.get(
    "/all-products",
    response_model=ProductResponseModel,
    # response_model_exclude_unset=True,
    response_description=" Get all products based on filters."
)
async def all_products(filter: ProductFilterModel = Depends()):
    query = {}
    if filter.search:
        query["title"] = {"$regex": re.compile(filter.search)}
    if filter.title:
        query["title"] = {"$search": filter.title}

    if filter.category:
        query["category"] = {"$eq": filter.category.lower()}
    if filter.categories:
        query["category"] = {"$in": filter.categories.split(",")}
    # if filter.brand:
    #     query["brand"] = {"$eq": filter.brand.lower()}
    # if filter.brands:
    #     query["brand"] = {"$in": filter.brands}

    if filter.min_price:
        query["price"] = {"$gte": filter.min_price}
    if filter.max_price:
        query["price"] = {"$lte": filter.max_price}

    # return filter
    (total, products) = await product_by_filter(query, filter)
    return {"total": total, "products": products}
