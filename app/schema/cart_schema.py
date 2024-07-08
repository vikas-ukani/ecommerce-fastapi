from pydantic import BaseModel
from datetime import datetime
from app.schema.product_schema import ProductModel


class CartBaseSchema(BaseModel):
    user_id: str
    total: int | None = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CartModel(CartBaseSchema):
    pass


class CartItemModel(BaseModel):
    id: str
    product_id: str
    user_id: str
    quantity: int
    cart_id: str
    product: ProductModel | None


class AddToCartSchema(BaseModel):
    product_id: str
    quantity: int | None = 1
