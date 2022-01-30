from injector import inject 
from dataclasses import dataclass
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from webauthn_server.adapters.gateway.sql_alchemy.database import session_scope

from webauthn_server.adapters.gateway.sql_alchemy.models.User import User
from webauthn_server.adapters.gateway.sql_alchemy.repository.readwrite_repository import ReadWriteRepository
from webauthn_server.entities.user.repository import IUserRepository
from webauthn_server.entities.user.schema import UserSchema


@inject
class UserRepository(ReadWriteRepository, IUserRepository):
    def __init__(self) -> None:
        super(UserRepository, self).__init__(User, UserSchema)

    def get_by_email(self, email: str) -> List[BaseModel]:
        with session_scope() as session:            
            return session.query(self.sql_alchemy_model).filter(self.sql_alchemy_model.email==email).first()
