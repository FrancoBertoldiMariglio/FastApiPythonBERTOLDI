"""
Module for Base Service
"""

from abc import ABC, abstractmethod
from typing import List

from models.base_model import BaseModel
from schemas.base_schema import BaseSchema
from repositories.base_repository import BaseRepository


class BaseService(ABC):
    """Base Service"""

    @property
    @abstractmethod
    def repository(self) -> BaseRepository:
        """
        Repository to access database
        """

    @property
    @abstractmethod
    def schema(self) -> BaseSchema:
        """
        Pydantic Schema to validate data
        """

    @property
    @abstractmethod
    def model(self) -> BaseModel:
        """
        SQLAlchemy Model
        """

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        """Get all"""

    @abstractmethod
    def get_one(self, id_key: int) -> BaseSchema:
        """Get by id"""

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save"""

    @abstractmethod
    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        """Update"""

    @abstractmethod
    def delete(self, id_key: int) -> None:
        """Delete"""

    @abstractmethod
    def to_model(self, schema: BaseSchema) -> BaseModel:
        """To model"""
