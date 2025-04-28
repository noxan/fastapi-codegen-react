import json
import subprocess
from pathlib import Path

from fastapi import FastAPI


def generate_schema(app: FastAPI):
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
