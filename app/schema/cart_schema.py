from pydantic import BaseModel
from datetime import datetime


class CartBaseSchema(BaseModel):
    user_id: str
    total: int | None = 0
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CartModel(CartBaseSchema):
    pass


class AddToCartSchema(BaseModel):
    product_id: str
    quantity: int | None = 1
