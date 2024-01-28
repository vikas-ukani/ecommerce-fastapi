from app.db import Product, serializeDict, serializeList
from app.log_manager import logger
from bson.objectid import ObjectId


async def product_by_filter(query: dict, filter):
    total = Product.count_documents(query)
    products = (
        Product.find(query)
        .sort(filter.sort_by, 1 if filter.descending is True else -1)
        .skip(filter.page)
        .limit(filter.limit)
    )
    return (total, serializeList(products))


def getProductById(id: str):
    return serializeDict(Product.find_one({"_id": ObjectId(id)}))
