import asyncio
from datetime import datetime

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from codegen import generate_schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    generate_schema(app)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
