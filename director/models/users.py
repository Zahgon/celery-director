import json

from sqlalchemy_utils import UUIDType
from sqlalchemy.types import PickleType

from director.extensions import db
from director.exceptions import UserNotFound
from director.models import BaseModel, StatusType
from director.models.utils import JSONBType


class User(BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def update(self):
        pass

    def delete(self):
        pass

    def to_dict(self):
        pass
