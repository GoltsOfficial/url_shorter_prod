from contextlib import asynccontextmanager

from fastapi import Body, FastAPI

from database.db import engine
from database.models import Base
from shortener import generate_random_slug


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/short_url")
async def generate_short_url(long_url: str = Body(embed=True)):
    slug = generate_random_slug()
    return {"data": slug}  # return short url


@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ...  # redirect
