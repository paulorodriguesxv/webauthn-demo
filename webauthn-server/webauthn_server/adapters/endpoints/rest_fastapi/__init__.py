from injector import Injector
from fastapi import FastAPI

from webauthn_server.adapters.endpoints.rest_fastapi.controllers import user_controller



def build(injector: Injector):
    app = injector.get(FastAPI)    
    app.include_router(user_controller.router,
                        prefix='/users',
                        tags=['users'])

    return app