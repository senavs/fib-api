from fastapi import FastAPI

from .database import DeclarativeBase, engine
from .erros import error_handler
from .routes import fibonacci
from .settings import settings
from .tasks import app as celery_app

# app
app = FastAPI(title=settings.PROJECT_NAME,
              description=settings.PROJECT_DESCRIPTION,
              version=settings.PROJECT_VERSION,
              docs_url=settings.URL_DOCS,
              redoc_url=settings.URL_REDOC)

# routes
app.include_router(fibonacci.router, prefix='/fib')

# database
DeclarativeBase.metadata.create_all(engine)

# handlers
error_handler(app)

# middleware
