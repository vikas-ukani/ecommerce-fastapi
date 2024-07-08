from pydantic import BaseModel
from typing import List


class CategoryModel(BaseModel):
    _id: str | None = None
    id: str | int = None
    slug: str | int = None
    name: str= None
    thumbnail: str = None
