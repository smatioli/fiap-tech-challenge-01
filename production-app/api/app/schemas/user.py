import re
from pydantic import validator, BaseModel
from datetime import datetime


class User(BaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value


class TokenData(BaseModel):
    access_token: str
    expires_at: datetime