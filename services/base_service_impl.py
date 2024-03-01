"""
Module for Base Service Implementation
"""
from typing import List, Type
from models.base_model import BaseModel
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from schemas.base_schema import BaseSchema


class BaseServiceImpl(BaseService):
    """ Base Service Implementation"""
    def __init__(self, repository: BaseRepository,
                 model: Type[BaseModel],
                 schema: Type[BaseSchema]):
        self.repository = repository
        self.model = model
        self.schema = schema

    @property
    def repository(self) -> BaseRepository:
        """Repository to access database"""
        return self._repository

    @property
    def schema(self) -> BaseSchema:
        """Pydantic Schema to validate data"""
        return self._schema

    @property
    def model(self) -> BaseModel:
        """SQLAlchemy Model"""
        return self._model

    def get_all(self) -> List[BaseSchema]:
        """Get all data"""
        return self.repository.find_all()

    def get_one(self, id_key: int) -> BaseSchema:
        """Get one data"""
        return self.repository.find(id_key)

    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save data"""
        return self.repository.save(self.to_model(schema))

    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        """Update data"""
        return self.repository.update(id_key, schema.model_dump())

    def delete(self, id_key: int) -> None:
        """Delete data"""
        self.repository.remove(id_key)

    def to_model(self, schema: BaseSchema) -> BaseModel:
        model_class = type(self.model) if not callable(self.model) else self.model
        model_instance = model_class(**schema.model_dump())
        return model_instance

    @repository.setter
    def repository(self, value):
        self._repository = value

    @model.setter
    def model(self, value):
        self._model = value

    @schema.setter
    def schema(self, value):
        self._schema = value
