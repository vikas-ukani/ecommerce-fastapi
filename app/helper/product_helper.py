from app.db import Product, serializeDict, serializeList
from app.log_manager import logger
from bson.objectid import ObjectId
from app.schema.product_schema import ProductFilterModel
import re

async def product_by_filter(filter: ProductFilterModel):
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

    logger.info(f"All Product Query: {query.__str__()}")
    total = Product.count_documents(query)
    print(f"filter.sort_by: {filter.page} {filter.sort_by}")
    products = (
        Product.find(query, {'id': False})
        .sort(filter.sort_by, 1 if filter.descending is True else -1)
        .skip((filter.page - 1) * filter.limit)
        # .skip(filter.page)
        .limit(filter.limit)
    )
    return (total, serializeList(products))


def getProductById(id: str):
    return serializeDict(Product.find_one({"_id": ObjectId(id)}))
