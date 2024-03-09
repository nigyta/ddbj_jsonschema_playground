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
    "dev": "test_schema.json",
    "ddbj_dev1": "ddbj_submission_dev1.json",
    "minimum": "example_schema_minimum.json",
    "submission_category": "data submission_category.json",
    "reference": "reference_schema.json",
    "multi_reference": "reference_schema_multi.json",
    "test": "example_schema.json",
    "test_2": "example_schema_1.json",
}

class Schema(str, Enum):
    DEV = 'dev'
    DEV1 = 'ddbj_dev1'
    MINIMUM = 'minimum'
    CATEGORY = 'submission_category'
    REFERENCE = 'reference'
    REFERENC2 = "multi_reference"
    TEST = 'test'
    TEST2 = 'test_2'

class SchemaType(BaseModel):
    name: Schema = Schema.DEV

class SchemaValidate(BaseModel):
    name: str
    data: dict

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get_schema_types")
async def get_schema_types():
    print(SchemaType.model_json_schema())
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

@app.post("/validate")
async def validate_schema(sc: SchemaValidate):
    print(sc)
    json_schema_file = json_schema_files[sc.name]
    with open(json_schema_file) as f:
        example_schema = json.load(f)
    try:
        validate(instance=sc.data, schema=example_schema)
        # print("validated")
        return {"status": "valid"}
    except ValidationError as e:
        print("validation failed")
        return {"status": "invalid", "message": e.message}

print(SchemaValidate.model_json_schema())