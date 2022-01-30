from abc import abstractmethod
from typing import List
from pydantic import BaseModel

from webauthn_server.entities.crud_repository import ICrudRepository

class IUserRepository(ICrudRepository):
    @abstractmethod
    def get_by_email(self, email: str) -> List[BaseModel]:
        pass
