from pydantic import BaseModel
from typing import List


class CategoryModel(BaseModel):
    title: str
    thumbnail: str
    images: List[str]
