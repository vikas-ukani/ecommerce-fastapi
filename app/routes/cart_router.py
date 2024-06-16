from app.lib.utils import get_current_user
from fastapi import APIRouter, Body, Depends
from ..schemas.cart import AddToCartSchema
from ..models.cart_helper import add_to_cart, get_cart_items, remove_cart_items
router = APIRouter()

@router.post('/add-to-cart', response_description="Add Item to cart")
async def addToCart(user=Depends(get_current_user), data: AddToCartSchema = Body()):
    await add_to_cart(user, data)
    cartItems = await get_cart_items(user)
    return cartItems

@router.get('/cart-items', response_description="Get All items from cart")
async def getCartItems(user=Depends(get_current_user)):
    return await get_cart_items(user)


@router.get('/remove-cart-items/{item_id}', response_description="Remove Item from cart")
async def getCartItems(item_id: str, user=Depends(get_current_user)):
    return await remove_cart_items(user, item_id)

