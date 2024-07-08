from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.middleware.log_middleware import LogMiddleware
from app.log_manager import logger

from app.route.auth_router import router as AuthRouter
from app.route.user_router import router as UserRouter
from app.route.product_router import router as ProductRouter
from app.route.category_router import router as CategoryRouter
from app.route.cart_router import router as CartRouter
from app.route.wishlist_router import router as WishlistRouter

# Seed Route
from app.route.seed_router import router as SeederRouter

app = FastAPI(debug=settings.DEBUG)

# Log Middleware.
# app.add_middleware(LogMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers={"*"},
)


@app.get("/", )
async def index():
    logger.info({"message": "logging from the root logger"})
    return {"message": "Welcome to the fast-api project."}


app.include_router(AuthRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")
app.include_router(ProductRouter, prefix="/api")
app.include_router(CategoryRouter, prefix="/api")
app.include_router(WishlistRouter, prefix="/api")
app.include_router(CartRouter, prefix="/api")

# SeederRouters
app.include_router(SeederRouter, prefix="/api")
