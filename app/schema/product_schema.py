from pydantic import BaseModel
from typing import List
from enum import Enum


class ProductDimensions(BaseModel):
    width: float
    height:float
    depth: float

class ProductReviews(BaseModel):
    rating: float =None
    comment: str =None
    date: str =None
    reviewerName: str =None
    reviewerEmail: str =None

class ProductMeta(BaseModel):
    createdAt: str =None
    updatedAt: str =None
    barcode: str =None
    qrCode: str =None
   

class ProductModel(BaseModel):
    _id: str | None = None
    id: int | str = None
    title: str = None
    sku: str = None
    weight: float = None
    description: str = None
    price: float = None
    discountPercentage: float = None
    rating: float = None
    stock: int = None
    brand: str = None
    category: str = None
    thumbnail: str = None
    images: List[str] = []
    tags: List[str] = []
    dimensions: ProductDimensions = None
    warrantyInformation: str = None
    shippingInformation: str = None
    availabilityStatus: str = None
    reviews: List[ProductReviews] = None
    returnPolicy: str = None
    minimumOrderQuantity: int = None
    meta: ProductMeta = None

class ProductResponseModel(BaseModel):
    products: List[ProductModel] = []
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
