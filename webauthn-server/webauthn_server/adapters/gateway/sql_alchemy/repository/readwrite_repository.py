from typing import List
from pydantic import BaseModel

from webauthn_server.adapters.gateway.sql_alchemy.database import SqlAlchemyBase, session_scope

class ReadWriteRepository():
    def __init__(self, sql_alchemy_model: SqlAlchemyBase, schema: BaseModel) -> None:
        self.sql_alchemy_model = sql_alchemy_model
        self.schema = schema

    def get_all(self) -> List[BaseModel]:
        with session_scope() as session:
            data = session.query(self.sql_alchemy_model).all()
            return list(map(self.schema.from_orm, data))

    def get_by_id(self, id: str) -> BaseModel:
        with session_scope() as session:
            return session.query(self.sql_alchemy_model).filter(self.sql_alchemy_model.id==id).first()

    def add(self, model: BaseModel) -> BaseModel:
        with session_scope() as session:
            db_data = self.sql_alchemy_model(**model.dict())    
            session.add(db_data)
            session.commit()
            session.refresh(db_data)

            return self.schema.from_orm(db_data)

    def delete(self, id: str):        
        with session_scope() as session:
            session.query(self.sql_alchemy_model).filter(self.sql_alchemy_model.id==id).delete()
            session.commit()
