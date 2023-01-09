from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel
import os 
import json


api = FastAPI()

class InnerObjectsModel(BaseModel):
    __root__: dict


# json model that accepts any dict and serializes it
class JsonModel(BaseModel):
    # root key of item
    __root__: dict


class JsonRootModel(BaseModel):
    __root__: dict[str, JsonModel] 

@api.post("/add_json")
async def add_json_data(json_data: JsonRootModel):
    # LOAD JSON FILE AND DUMP JSON_DATA TO FILE
    with open("db.json", "r") as file:
        data = json.load(file)
  
    # file data manipulation
    new_data = json_data.dict()
    data["__root__"]["accounts"].update(new_data["__root__"]["accounts"])

    with open("db.json", "w") as file:
        json.dump(data, file)

    print(data)

    return JsonModel.parse_obj(data)

@api.get("/")
async def get_data():
    with open("./db.json", "r") as file:
        data = json.load(file)
    return dict(data)
