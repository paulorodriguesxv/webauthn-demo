from injector import Injector
from sqlalchemy.orm import Session

from webauthn_server.adapters.gateway.sql_alchemy.database import session_scope
from webauthn_server.adapters.gateway.sql_alchemy.repository.user_repository import UserRepository
from webauthn_server.business_rules.exceptions.user_exceptions import EUserEmailAlreadyExists

from webauthn_server.business_rules.use_cases.user_use_case import UserUseCase
from webauthn_server.entities.user.repository import IUserRepository
from .entities.user.schema import UserSchema

# for fast api
from webauthn_server.adapters.endpoints import rest_fastapi

def configure(binder):
    binder.bind(Session, to=session_scope)
    binder.bind(IUserRepository, to=UserRepository)    
    binder.bind(UserUseCase, to=UserUseCase)

injector = Injector([configure])

app = rest_fastapi.build(injector=injector)