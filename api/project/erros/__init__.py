from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from .exception import BadRequestAPIException, NotFoundAPIException


def error_handler(app: FastAPI):
    @app.exception_handler(400)
    def error_handler_400(request: Request, err: HTTPException):
        return JSONResponse(status_code=400, content={'message': f'Bad request - {err}', 'status': 400})

    @app.exception_handler(404)
    def error_handler_404(request: Request, err: HTTPException):
        return JSONResponse(status_code=404, content={'message': 'Page not found', 'status': 404})

    @app.exception_handler(500)
    def error_handler_500(request: Request, err: HTTPException):
        return JSONResponse(status_code=500, content={'message': f'Internal server error - {err}', 'status': 500})

    @app.exception_handler(Exception)
    def error_handler_exception(request: Request, err: Exception):
        return JSONResponse(status_code=500, content={'message': f'Internal server error - {err}', 'status': 500})

    @app.exception_handler(BadRequestAPIException)
    def error_handler_exception(request: Request, err: BadRequestAPIException):
        return JSONResponse(status_code=err.code, content={'message': err.message, 'status': err.code})

    @app.exception_handler(NotFoundAPIException)
    def error_handler_exception(request: Request, err: NotFoundAPIException):
        return JSONResponse(status_code=err.code, content={'message': err.message, 'status': err.code})
