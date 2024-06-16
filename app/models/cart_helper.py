from app.db import Cart, CartItem
from app.db import serializeDict, serializeList
from bson import ObjectId

async def create_cart(user):
    cart = Cart.insert_one({
        'user_id': user['_id'],
        'total': 0
    })
    return serializeDict(Cart.find_one({'_id': cart.inserted_id}))

async def get_cart(user):
    cart = Cart.find_one({'user_id': user['_id']})
    if not cart:
        cart = await create_cart(user)
    return serializeDict(cart)


async def add_to_cart(user, data: dict):
    cart = await get_cart(user)
    existingCartItem = CartItem.find_one({'product_id': data.product_id, 'user_id': user['_id']})
    if not existingCartItem:
        CartItem.insert_one({
            'product_id': data.product_id,
            'user_id': user['_id'],
            'quantity': data.quantity,
            'cart_id': cart['_id'],
        })
    else:
        CartItem.update_one({
            'product_id': data.product_id,
            'user_id': user['_id'],
            'cart_id': cart['_id'],
        },
        {
            "$set": {
                'quantity': existingCartItem['quantity'] + data.quantity
            }
        })


async def get_cart_items(user):
    return serializeList(CartItem.find({'user_id': user['_id']}))


async def remove_cart_items(user, item_id):
    query = {'_id': ObjectId(item_id), 'user_id': user['_id']}
    item = CartItem.find_one(query)
    if item:
        CartItem.delete_one(query)
        return True
    return False