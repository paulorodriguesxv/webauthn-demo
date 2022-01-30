from injector import Injector
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from webauthn_server.adapters.gateway.sql_alchemy.database import session_scope
from webauthn_server.adapters.gateway.sql_alchemy.repository.user_repository import UserRepository
from webauthn_server.business_rules.exceptions.user_exceptions import EUserEmailAlreadyExists

from webauthn_server.business_rules.use_cases.user_use_case import UserUseCase
from webauthn_server.entities.user.repository import IUserRepository
from .entities.user.schema import UserSchema

def configure(binder):
    binder.bind(Session, to=session_scope)
    binder.bind(IUserRepository, to=UserRepository)    
    binder.bind(UserUseCase, to=UserUseCase)

injector = Injector([configure])

app = injector.get(FastAPI)

def get_uc(user_case):
    return injector.get(user_case)


@app.get("/users", response_model=List[UserSchema])
async def users():
    user_use_case = injector.get(UserUseCase)
    user_c = await user_use_case.get_all()
    
    return user_c

@app.get("/users/{user_id}", response_model=UserSchema)
async def users(user_id: str):
    user_use_case = injector.get(UserUseCase)
    user_c = await user_use_case.get_user(user_id)
    
    return user_c


@app.post("/users", response_model=UserSchema)
async def users(user: UserSchema):
    user_use_case = injector.get(UserUseCase)
    try:
        user_c = await user_use_case.register_user(user)
    except EUserEmailAlreadyExists:
        raise HTTPException(status_code=422, detail="Email já existente")
    
    return user_c


@app.delete("/users/{user_id}")
async def users(user_id: str):
    user_use_case = injector.get(UserUseCase)
    await user_use_case.delete(user_id)
    