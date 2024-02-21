import json 
from jsonschema import validate, ValidationError


# json_schema_file = "example_schema_1.json"
json_schema_file = "example_schema.json"

with open(json_schema_file) as f:
    example_schema = json.load(f)

metadata = {
    "data_type": "genome",
    "bioproject": "PRJAD0000001",
    "division": "CON",
    "keyword": ["WGS", "STANDARD_DRAFT"],
    "sra": ["DRR000001", "ERR000001"],
    "assembly": "test"
}

# Show schema
# print(json.dumps(example_schema, indent=4))

try:
    validate(metadata, example_schema)
    print(f"validation success")
except ValidationError as e:
    print(e.message)
