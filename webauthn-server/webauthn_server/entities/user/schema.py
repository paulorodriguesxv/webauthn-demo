from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import Optional

def get_uuid():
    return uuid4().hex


class UserSchema(BaseModel):
    id: str = Field(default_factory=get_uuid)
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        orm_mode = True