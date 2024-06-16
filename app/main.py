from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from app.middleware.log_middleware import LogMiddleware
from app.log_manager import logger
from .routes.auth import router as AuthRouter
from .routes.users import router as UserRouter
from .routes.products import router as ProductRouter
from .routes.category import router as CategoryRouter
from .routes.cart_router import router as CartRouter
# Seed Route
from .routes.seed import router as SeederRouter

app = FastAPI(debug=config("DEBUG"))

# Log Middleware.
# app.add_middleware(LogMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers={"*"},
)


@app.get("/")
async def index():
    logger.info({"message": "logging from the root logger"})
    return {"message": "Welcome to the fast-api project."}


app.include_router(AuthRouter)
app.include_router(UserRouter)
app.include_router(ProductRouter)
app.include_router(CategoryRouter)
app.include_router(CartRouter)

# SeederRouters
app.include_router(SeederRouter)
