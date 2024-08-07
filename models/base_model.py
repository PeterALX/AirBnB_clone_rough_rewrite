#!/usr/bin/python3
"""
The base class for all hbnb models is defined here
"""
from datetime import datetime, timedelta
from uuid import uuid4

class BaseModel:
    """
    The base for all hbnb models
    all hbnb models extend this class
      Attributes:
        id (uuid string): The model id.
        created_at (datetime): The datetime at creation.
        updated_at (datetime): The datetime of last update.
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at 
    
    def __str__(self):
        """ Return a string representation of the BaseModel instance """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """
        persists changes made to a BaseModel instance in future
        and reflects the time of update
        -> persisting not implemented yet
        """
        self.updated_at = datetime.now()
    def to_dict(self):
        """
        returns a json serealizable dictionary representation
        of an instance
        """
        d = {}
        d['__class__'] = self.__class__.__name__ 
        for k,v in self.__dict__.items():
            if type(v) is datetime:
                d[k] = v.isoformat() 
            else:
                d[k] = v
        return (d)
