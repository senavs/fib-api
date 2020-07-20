from datetime import datetime
from typing import List, Optional, Union

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship, backref, validates

from . import DeclarativeBase
from .base import BaseModel
from .connector import Connector
from ..erros.exception import BadRequestAPIException, NotFoundAPIException


class Fibonacci(DeclarativeBase, BaseModel):
    __tablename__ = 'FIBONACCI'

    ID_FIBONACCI = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    LT_FIBONACCI = Column(Text, nullable=False, unique=False, default='')
    IN_FINISHED = Column(Boolean, nullable=False, unique=False, default=False)
    IN_VIEWED = Column(Boolean, nullable=False, unique=False, default=False)
    DT_CREATED = Column(DateTime, nullable=False, unique=False, default=datetime.utcnow)
