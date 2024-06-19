from pydantic import BaseModel
from typing import List
from enum import Enum


class ProductBaseModel(BaseModel):
    id: int = None
    title: str = None
    description: str = None
    price: int = None
    discountPercentage: float = None
    rating: float = None
    stock: int = None
    brand: str = None
    category: str = None
    thumbnail: str = None
    images: List[str] = []

class ProductResponseModel(BaseModel):
    products: List[ProductBaseModel] = []
    total: int


class ProductSortBy(str, Enum):
    created_at = "created_at"
    title = "title"
    category = "category"
    price = "price"
    rating = "rating"
    stock = "stock"


class PriceFilterModel(BaseModel):
    min: float | None = 0
    max: float | None = 9999


class ProductFilterModel(BaseModel):
    search: str | None = None
    title: str | None = None
    category: str | None = None
    categories: str | None = None
    brand: str | None = None
    # brands: List[str] = []
    min_price: float | None = None
    max_price: float | None = None
    page: int | None = 1
    limit: int | None = 10
    sort_by: ProductSortBy | None = ProductSortBy.title
    descending: bool = False
