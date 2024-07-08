from app.lib.utils import get_current_user
from fastapi import APIRouter, Body, Depends
from ..schema.cart_schema import AddToCartSchema, CartItemModel
from ..helper.cart_helper import add_to_cart, get_cart_items, remove_cart_items, update_cart_total_amount
from typing import List
router = APIRouter()


@router.post('/add-to-cart', response_model=List[CartItemModel], response_description="Add Item to cart")
async def addToCart(user=Depends(get_current_user), data: AddToCartSchema = Body()):
    cart = await add_to_cart(user, data)
    cartItems = await get_cart_items(user)
    await update_cart_total_amount(cart, cartItems)
    return cartItems


@ router.get('/cart-items', response_model=List[CartItemModel], response_description="Get All items from cart")
async def getCartItems(user=Depends(get_current_user)):
    return await get_cart_items(user)


@ router.delete('/remove-cart-items/{item_id}', response_model=List[CartItemModel], response_description="Remove Item from cart")
async def getCartItems(item_id: str, user=Depends(get_current_user)):
    deleted = await remove_cart_items(user, item_id)
    if deleted:
        return await get_cart_items(user)
    return None
