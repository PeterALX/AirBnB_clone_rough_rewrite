#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *ar, **kw):
        if kw:
            for k, v in kw.items():
                # potential oversight: what if key is int
                # potential oversight: test for a dict without the expected
                #   keys/variables?
                # potential oversight: test for a dict without expected
                # keys/variables?
                # should add these to tests?
                if k in ['created_at', 'updated_at']:
                    # 👆what if other attrs are dates?
                    setattr(self, k, datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()
            else:
                d[k] = v
        d['__class__'] = self.__class__.__name__
        return (d)
