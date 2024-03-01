"""
BaseRepository is an abstract class that defines the methods
"""
from abc import abstractmethod, ABC
from typing import List, Type
from sqlalchemy.orm import Session

from models.base_model import BaseModel
from schemas.base_schema import BaseSchema


class BaseRepository(ABC):
    """
    BaseRepository is an abstract class that defines the methods
    that must be implemented by the repositories.
    """
    @property
    @abstractmethod
    def session(self) -> Session:
        """
        SQLAlchemy session
        """

    @property
    @abstractmethod
    def model(self) -> Type[BaseModel]:
        """
        SQLAlchemy model
        """

    @property
    @abstractmethod
    def schema(self) -> Type[BaseSchema]:
        """
        Pydantic schema
        """

    @abstractmethod
    def find(self, id_key: int) -> BaseSchema:
        """
        Find a record by id_key
        :param id_key: int
        :return: BaseSchema
        """

    @abstractmethod
    def find_all(self) -> List[BaseSchema]:
        """
        Find all records
        :return: List[BaseSchema]
        """

    @abstractmethod
    def save(self, model: BaseModel) -> BaseSchema:
        """
        Save a record
        :param model: BaseModel
        :return: BaseSchema
        """

    @abstractmethod
    def update(self, id_key: int, changes: dict) -> BaseSchema:
        """
        Update a record
        :param id_key: int
        :param model: BaseModel
        :return: BaseSchema
        """

    @abstractmethod
    def remove(self, id_key: int) -> None:
        """
        Delete a record by id_key
        :param id_key: int
        """

    @abstractmethod
    def save_all(self, models: List[BaseModel]) -> List[BaseSchema]:
        """
        Save multiple records
        :param models: List[BaseModel]
        :return: List[BaseSchema]
        """
