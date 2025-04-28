import asyncio

from datetime import datetime
import json
from pathlib import Path
import subprocess

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI app"""
    schema_definition = app.openapi()

    schema_path = Path(".schema")
    schema_path.mkdir(exist_ok=True)

    with open(schema_path / "openapi.json", "w") as f:
        json.dump(schema_definition, f, indent=2)

    subprocess.run(
        [
            "bun",
            "run",
            "openapi-typescript",
            schema_path / "openapi.json",
            "-o",
            schema_path / "openapi.d.ts",
        ]
    )
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": f"Hello World at {datetime.now().isoformat()}"}
