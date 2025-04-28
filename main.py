import asyncio

from datetime import datetime

from fastapi import FastAPI

from codegen import lifespan


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": f"Hello World at {datetime.now().isoformat()}"}
