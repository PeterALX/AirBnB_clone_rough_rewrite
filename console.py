#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage

print(storage.all())
tst = BaseModel()
print(storage.all())
tst.save()
