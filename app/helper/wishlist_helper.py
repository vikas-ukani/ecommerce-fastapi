from app.db import Wishlist, serializeList, serializeDict
from app.log_manager import logger
from bson import ObjectId
from app.db import Product


async def fetch_wishlist(user):
    wishlists = serializeList(Wishlist.find({'user_id': user['_id']}))
    for wishlist in wishlists:
        product = None
        if ObjectId.is_valid(wishlist['product_id']):
            product = Product.find_one({'_id': ObjectId(wishlist['product_id'])}, {"id": False})
            # del product['id']
        wishlist['product'] = serializeDict(product) if product else None
    return serializeList(wishlists)


async def create_wishlist(user, data):
    existing_wishlist = Wishlist.find_one(
        {'user_id': user['_id'], 'product_id': data.product_id})

    if not existing_wishlist:
        new_wishlist = Wishlist.insert_one({
            'user_id': user['_id'],
            'product_id': data.product_id,
            'created_at': data.created_at,
            'updated_at': data.updated_at,
        })
        wishlist = Wishlist.find_one({'_id': new_wishlist.inserted_id})
        return serializeDict(wishlist)
    return serializeDict(existing_wishlist)


async def delete_wishlist(user, wishlist_id):
    query = {'_id': ObjectId(wishlist_id), 'user_id': user['_id']}
    found = Wishlist.find_one(query)
    if not found:
        return False
    Wishlist.delete_one(query)
    return True
