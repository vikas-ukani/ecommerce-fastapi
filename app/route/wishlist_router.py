from app.lib.utils import get_current_user
from fastapi import APIRouter, Depends, Body
from app.helper.wishlist_helper import fetch_wishlist, create_wishlist, delete_wishlist
from app.schema.wishlist_schema import WishlistModel, AddWishlistSchema
from typing import List

router = APIRouter()


@router.get('/wishlist', response_model=List[WishlistModel])
async def get_wishlists(user= Depends(get_current_user)):
    return await fetch_wishlist(user)


@router.post('/wishlist', response_model=WishlistModel)
async def addWishlist(user = Depends(get_current_user), wishlist: AddWishlistSchema = Body()):
    return await create_wishlist(user, wishlist)


@router.delete('/wishlist/{wishlist_id}', response_model=bool, response_description="Remove Item from wishlist")
async def remove_wishlist(wishlist_id: str, user = Depends(get_current_user)):
    return await delete_wishlist(user, wishlist_id)