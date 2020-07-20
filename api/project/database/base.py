from typing import Optional

from . import DeclarativeBase
from .connector import Connector

from ..erros.exception import NotFoundAPIException


class BaseModel:

    @classmethod
    def find_by_id(cls, connection: Connector, identifier: int, raise_not_found: bool = True) -> DeclarativeBase:
        result = connection.query(cls).get(identifier)
        if not result and raise_not_found:
            raise NotFoundAPIException(f'id {identifier} not found')
        return result

    @classmethod
    def find_all(cls, connection: Connector) -> DeclarativeBase:
        return connection.query(cls).all()

    def add(self, connection: Connector):
        connection.session.add(self)
        connection.session.commit()

    def delete(self, connection: Connector):
        connection.session.delete(self)
        connection.session.commit()

    def to_dict(self, *, exclude: Optional[list] = None) -> dict:
        if not exclude:
            exclude = []
        return {attr.lower(): getattr(self, attr) for attr in self.__dir__() if attr.isupper() and attr not in exclude}

    def __repr__(self):
        return f'{type(self).__qualname__}({self.to_dict()})'
