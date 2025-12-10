from fastapi import FastAPI
from contextlib import asynccontextmanager
import app.load_data.load as d
from app.routers.products import router as products_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    d.load_products_data()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(products_router)

@app.get("/")
def greet():
    return "Welcome Kabira! Please focus on your growth."
