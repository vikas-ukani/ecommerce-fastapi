from app.db import Cart, CartItem, Product
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
    existingCartItem = CartItem.find_one(
        {'product_id': data.product_id, 'user_id': user['_id']})
    if not existingCartItem:
        CartItem.insert_one({
            'product_id': data.product_id,
            'user_id': user['_id'],
            'quantity': data.quantity,
            'cart_id': cart['_id'],
        })
    else:
        quantity = existingCartItem['quantity'] + data.quantity
        if quantity == 0:
            await remove_cart_items(user, str(existingCartItem['_id']))
        else:
            CartItem.update_one({
                'product_id': data.product_id,
                'user_id': user['_id'],
                'cart_id': cart['_id'],
            },
                {
                "$set": {
                    'quantity': quantity
                }
            })
    return cart


async def get_cart_items(user):
    cartItems = serializeList(CartItem.find({'user_id': user['_id']}))
    for cartItem in cartItems:
        product = Product.find_one(
            {'_id': ObjectId(cartItem['product_id'])})
        del product['id']
        cartItem['product'] = serializeDict(product)
    return serializeList(cartItems)


async def update_cart_total_amount(cart, cartItems):
    total = 0
    for cartItem in cartItems:
        total += cartItem['product']['price'] * cartItem['quantity']
    Cart.update_one({'_id': ObjectId(cart['_id'])}, {'$set': {'total': total}})


async def remove_cart_items(user, item_id):
    query = {'_id': ObjectId(item_id), 'user_id': user['_id']}
    item = CartItem.find_one(query)
    if item:
        CartItem.delete_one(query)
        return True
    return False
