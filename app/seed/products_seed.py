import requests
from app.db import Product

PRODUCTS_SEED_URL = "https://dummyjson.com/products?limit=2000"


async def seed_products_data():
    response = requests.get(PRODUCTS_SEED_URL)
    data = response.json()

    if data['products']:
        # Delete all documents and re-seed.
        Product.delete_many({})

        Product.insert_many(data['products'])


# if __name__ == '__main__':
#     seed_products_data()
