"""Base controller implementation module."""
from typing import Type, List
from fastapi import APIRouter, HTTPException
from controllers.base_controller import BaseController
from schemas.base_schema import BaseSchema
from services.base_service import BaseService


class BaseControllerImpl(BaseController):
    """Base controller implementation."""

    def __init__(self, schema: Type[BaseSchema], service: BaseService,):
        self.service = service
        self.schema = schema
        self.router = APIRouter()

        @self.router.get("/", response_model=List[schema])
        async def get_all():
            return self.get_all()

        @self.router.get("/{id_key}", response_model=schema)
        async def get_one(id_key: int):
            item = self.get_one(id_key)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.post("/", response_model=schema)
        async def save(schema_in: schema):
            return self.save(schema_in)

        @self.router.put("/{id_key}", response_model=schema)
        async def update(id_key: int, schema_in: schema):
            item = self.update(id_key, schema_in)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.delete("/{id_key}")
        async def delete(id_key: int):
            self.delete(id_key)

    @property
    def service(self) -> BaseService:
        """Service to access database."""
        return self._service

    @property
    def schema(self) -> Type[BaseSchema]:
        """Pydantic Schema to validate data."""
        return self._schema

    def get_all(self) -> List[BaseSchema]:
        """Get all data."""
        return self.service.get_all()

    def get_one(self, id_key: int) -> BaseSchema:
        """Get one data."""
        return self.service.get_one(id_key)

    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save data."""
        return self.service.save(schema)

    def update(self, id_key: int, schema: BaseSchema) -> BaseSchema:
        """Update data."""
        return self.service.update(id_key, schema)

    def delete(self, id_key: int) -> None:
        """Delete data."""
        self.service.delete(id_key)

    @schema.setter
    def schema(self, value):
        self._schema = value

    @service.setter
    def service(self, value):
        self._service = value
