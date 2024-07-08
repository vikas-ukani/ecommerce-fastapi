import requests
from app.db import Category, Product

CATEGORIES_SEED_URL = "https://dummyjson.com/products/categories?limit=2000"

async def seed_categories_data():

    response = requests.get(CATEGORIES_SEED_URL)
    categories = response.json()

    for category in categories:
        product = Product.find_one({'category': category['slug']})
        category['thumbnail'] = product['thumbnail']

    # Remove all existing record before seed.
    Category.delete_many({})
    Category.insert_many(categories)
