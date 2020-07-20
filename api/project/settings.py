from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # project
    PROJECT_NAME: Optional[str] = 'Fibonacci API'
    PROJECT_DESCRIPTION: Optional[str] = 'Generate Fibonacci sequence with Python, message broker and nginx'
    PROJECT_VERSION: Optional[str] = '1.0.0'
    # url
    URL_DOCS: Optional[str] = '/docs'
    URL_REDOC: Optional[str] = None
    # database
    URI_DATABASE: str
    # celery
    CELERY_RESULT_BACKEND: Optional[str] = None
    CELERY_BROKER_URL: Optional[str] = None


settings = Settings()
