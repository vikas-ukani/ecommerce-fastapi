from pydantic import BaseModel, Field
from app.schema.product_schema import ProductModel
from datetime import datetime


class WishlistModel(BaseModel):
    id: str | None = None
    user_id: str
    product_id: str
    created_at: datetime = None
    updated_at: datetime = None


class GetWishlistModel(WishlistModel):
    product: ProductModel | None


class AddWishlistSchema(BaseModel):
    product_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
