"""
Module for the abstract base controller class.
"""

from abc import ABC, abstractmethod
from typing import Type, List

from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseController(ABC):
    """
    Abstract base controller class.
    """

    @property
    @abstractmethod
    def service(self) -> BaseService:
        """
        Service to access database
        """

    @property
    @abstractmethod
    def schema(self) -> Type[BaseSchema]:
        """
        Pydantic Schema to validate data
        """

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        """
        Get all data
        """

    @abstractmethod
    def get_one(self, id_key: int) -> BaseSchema:
        """
        Get one data
        """

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        """
        Save data
        """

    @abstractmethod
    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        """
        Update data
        """

    @abstractmethod
    def delete(self, id_key: int) -> None:
        """
        Delete data
        """
