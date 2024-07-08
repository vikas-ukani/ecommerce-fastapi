from fastapi import APIRouter, Depends, HTTPException, status
from app.schema.product_schema import ProductFilterModel, ProductResponseModel, ProductModel
from app.helper.product_helper import product_by_filter, getProductById
from app.log_manager import logger

router = APIRouter()


@router.get("/product/{id}", response_model=ProductModel, response_description="Get product by id")
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
    (total, products) = await product_by_filter(filter)
    return ProductResponseModel(products=products, total=total)
    # return {"total": total, "products": products}
