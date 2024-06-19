from app.db import Category, serializeList


async def fetch_categories():
    return serializeList(Category.find({}))
