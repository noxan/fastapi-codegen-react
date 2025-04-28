import asyncio

from datetime import datetime

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from codegen import generate_schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_schema(app)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": f"Hello World at {datetime.now().isoformat()}"}
