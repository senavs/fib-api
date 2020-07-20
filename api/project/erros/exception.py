class BaseAPIException(Exception):
    code: int = 500
    message: str = ''

    def __init__(self, message: str):
        self.message = message


class BadRequestAPIException(BaseAPIException):
    code: int = 400


class NotFoundAPIException(BaseAPIException):
    code: int = 404
