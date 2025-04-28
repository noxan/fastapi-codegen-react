import asyncio

from datetime import datetime

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from pydantic import BaseModel

from codegen import generate_schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_schema(app)
    yield


app = FastAPI(lifespan=lifespan)


class MessageSchema(BaseModel):
    message: str
    timestamp: datetime


@app.get("/")
async def root() -> MessageSchema:
    await asyncio.sleep(0.1)
    return MessageSchema(
        message="Hello World",
        timestamp=datetime.now(),
    )
