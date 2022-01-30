from injector import inject
from dataclasses import dataclass
from sqlalchemy.orm import Session
from webauthn_server.business_rules.exceptions.user_exceptions import EUserEmailAlreadyExists
from webauthn_server.entities.user.repository import IUserRepository
from webauthn_server.entities.user.schema import UserSchema

@inject
@dataclass
class UserUseCase():
    user_repository: IUserRepository
    async def register_user(self, user: UserSchema):
        user_found = self.user_repository.get_by_email(user.email)
        if user_found:
            raise EUserEmailAlreadyExists()
        return self.user_repository.add(user)
    
    async def get_user(self, user_id: str):
        return self.user_repository.get_by_id(user_id)

    async def get_all(self):
        return self.user_repository.get_all()

    async def delete(self, user_id: str):
        return self.user_repository.delete(user_id)