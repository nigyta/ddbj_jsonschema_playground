# DDBJ JSONschema Playground

DDBJ JSON schema 開発のための実験用レポジトリ
JSON schemaを使ったvalidationとフォーム自動生成の試作を行う

Experimental playground for the development of DDBJ JSON schema


### Implementation
- Backend: Python, FastAPI, pyjsonchema
- Frontend: React, React Json Schema Form, axios, bootstrap

## Quick Start

1. Get the source code  
```
git clone git@github.com:nigyta/ddbj_jsonschema_playground.git

or

git clone https://github.com/nigyta/ddbj_jsonschema_playground.git
```

2. Build the Docker containers  
```
cd ddbj_jsonschema_playground
docker-compose -f docker-compose-dev.yml build
```
or
```
docker-compose build
```
This may take time since it includes installation of React and its related libraries, which is not included in `docker-compose-dev.yml`  

3. Installation of React and its related libraries
```
docker-compose run frontend npm install
```
This will install the modules under `frontend/react_jsonschema/node_modules`

4. Launch  
```
docker-compose up
```

5. Access the services  
Open http://localhost:8000/docs for API specs.  
Open http://localhost:3000 to access the web form automaticcaly generated based on the definition of JSON schema.

## How to edit JSON schema  
JSON schema files are located under `backend`.
To add a schema, create a JSON file and edit the part below in `backend/main.py`.  
```
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
```

## Development within containers using VSCode
`Open Folder in Container` and choose `frontend` or `backend` (or both in different windows). The services wil automatically start and you can start editing the code.  
For the first time, you need to install the Remote - Containers extension.  


