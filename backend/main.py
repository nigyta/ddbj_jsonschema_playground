from fastapi import FastAPI
import json 
from jsonschema import validate, ValidationError
from fastapi.middleware.cors import CORSMiddleware

# for defining the pydantic model
from pydantic import BaseModel, Field
from typing import Literal
from enum import Enum

# general API settings
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可する場合
    allow_credentials=True,
    allow_methods=["*"],  # 全てのメソッド（GET, POST, PUT, DELETE等）を許可する場合
    allow_headers=["*"],  # 全てのヘッダーを許可する場合
)


# To add Json schema file, update this dictionary and Schema class
json_schema_files = {
    "reference": "reference_schema.json",
    "test": "example_schema.json",
    "test_2": "example_schema_1.json"
}

class Schema(str, Enum):
    REFERENCE = 'reference'
    TEST = 'test'
    TEST2 = 'test_2'

class SchemaType(BaseModel):
    name: Schema = Schema.REFERENCE

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get_schema_types")
async def get_schema_types():
    return SchemaType.model_json_schema()


@app.post("/schema")
async def get_schema(schema_type: SchemaType):
    json_schema_file = json_schema_files[schema_type.name]
    print(schema_type)
    print(schema_type.name)
    with open(json_schema_file) as f:
        example_schema = json.load(f)
    # print(schema_type.model_json_schema())
    return example_schema