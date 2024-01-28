from app.db import Category

_categories_seed_data = [
    {
        "title": "Smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/1/1.jpg",
            "https://cdn.dummyjson.com/product-images/1/2.jpg",
            "https://cdn.dummyjson.com/product-images/1/3.jpg",
            "https://cdn.dummyjson.com/product-images/1/4.jpg",
            "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        ],
    },
    {
        "title": "laptops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/6/thumbnail.png",
        "images": [
            "https://cdn.dummyjson.com/product-images/6/1.png",
            "https://cdn.dummyjson.com/product-images/6/2.jpg",
            "https://cdn.dummyjson.com/product-images/6/3.png",
            "https://cdn.dummyjson.com/product-images/6/4.jpg",
        ],
    },
    {
        "title": "home-decoration",
        "thumbnail": "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/26/1.jpg",
            "https://cdn.dummyjson.com/product-images/26/2.jpg",
            "https://cdn.dummyjson.com/product-images/26/3.jpg",
            "https://cdn.dummyjson.com/product-images/26/4.jpg",
            "https://cdn.dummyjson.com/product-images/26/5.jpg",
            "https://cdn.dummyjson.com/product-images/26/thumbnail.jpg",
        ],
    },
    {
        "title": "furniture",
        "thumbnail": "https://cdn.dummyjson.com/product-images/31/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/31/1.jpg",
            "https://cdn.dummyjson.com/product-images/31/2.jpg",
            "https://cdn.dummyjson.com/product-images/31/3.jpg",
            "https://cdn.dummyjson.com/product-images/31/4.jpg",
            "https://cdn.dummyjson.com/product-images/31/thumbnail.jpg",
        ],
    },
    {
        "title": "mens-shoes",
        "thumbnail": "https://cdn.dummyjson.com/product-images/56/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/56/1.jpg",
            "https://cdn.dummyjson.com/product-images/56/2.jpg",
            "https://cdn.dummyjson.com/product-images/56/3.jpg",
            "https://cdn.dummyjson.com/product-images/56/4.jpg",
            "https://cdn.dummyjson.com/product-images/56/5.jpg",
            "https://cdn.dummyjson.com/product-images/56/thumbnail.jpg",
        ],
    },
    {
        "title": "womens-bags",
        "thumbnail": "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/71/1.jpg",
            "https://cdn.dummyjson.com/product-images/71/2.jpg",
            "https://cdn.dummyjson.com/product-images/71/3.webp",
            "https://cdn.dummyjson.com/product-images/71/thumbnail.jpg",
        ],
    },
    {
        "title": "lighting",
        "thumbnail": "https://cdn.dummyjson.com/product-images/96/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/96/1.jpg",
            "https://cdn.dummyjson.com/product-images/96/2.jpg",
            "https://cdn.dummyjson.com/product-images/96/3.jpg",
            "https://cdn.dummyjson.com/product-images/96/4.jpg",
            "https://cdn.dummyjson.com/product-images/96/thumbnail.jpg",
        ],
    },
    {
        "title": "tops",
        "thumbnail": "https://cdn.dummyjson.com/product-images/36/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/36/1.jpg",
            "https://cdn.dummyjson.com/product-images/36/2.webp",
            "https://cdn.dummyjson.com/product-images/36/3.webp",
            "https://cdn.dummyjson.com/product-images/36/4.jpg",
            "https://cdn.dummyjson.com/product-images/36/thumbnail.jpg",
        ],
    },
    {
        "title": "mens-shirts",
"thumbnail": "https://cdn.dummyjson.com/product-images/51/thumbnail.jpg",
"images": [
"https://cdn.dummyjson.com/product-images/51/1.png",
"https://cdn.dummyjson.com/product-images/51/2.jpg",
"https://cdn.dummyjson.com/product-images/51/3.jpg",
"https://cdn.dummyjson.com/product-images/51/thumbnail.jpg"
]
    }
]


async def seed_categories_data():
    await Category.insert_many(_categories_seed_data)
