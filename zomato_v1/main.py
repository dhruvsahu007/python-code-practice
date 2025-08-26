from fastapi import FastAPI
from database import engine, Base
import models
from routes import router as restaurants_router

app = FastAPI(title="Zomato V1 - Restaurant Management")

app.include_router(restaurants_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Zomato V1 - Restaurant Management API"}


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    await init_db()


