from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..settings import settings

# basic
engine = create_engine(settings.URI_DATABASE, echo=False)
DeclarativeBase = declarative_base()
Session = sessionmaker(engine)
