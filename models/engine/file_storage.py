#!/usr/bin/python3
"""
FileStorage Engine
-> Stores data in a json file
"""
import json


class FileStorage:
    __file_path = 'db.json'
    __objects = {}

    def all(self):
        return (self.__objects)  # pass by reference ok?

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                from models.base_model import BaseModel
                classes = {
                        'BaseModel': BaseModel
                        }
                json_dict = json.load(f)
                for k, v in json_dict.items():
                    self.__objects[f'{k}'] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass
