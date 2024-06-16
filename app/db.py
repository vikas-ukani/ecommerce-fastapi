# from motor import motor_asyncio
from decouple import config
from pymongo import MongoClient

client = MongoClient(config('MONGO_URL'))
db = client["fast-com"]

# Models
User = db.get_collection("users")
Product = db.get_collection("products")
Category = db.get_collection("categories")
Cart = db.get_collection("carts")
CartItem = db.get_collection("cart_items")


def serializeDict(object: dict) -> dict:
    return {
        **{key: str(object[key]) for key in object if key == "_id"},
        **{otherKey: object[otherKey] for otherKey in object if otherKey != "_id"},
    }

def serializeList(lists: list) -> list:
    return [serializeDict(list) for list in lists]
