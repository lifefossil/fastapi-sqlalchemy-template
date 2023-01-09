from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapicf import settings
from fastapi.staticfiles import StaticFiles
from src.router.router import AllRouter
from src.core.events import startup, stopping
from src.exception.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, \
    UnicornException
from src.middleware.fastapi_middleware import Middleware
import uvicorn

# 初始化项目
application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME,
)

# 事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))

# http异常错误处理
application.add_exception_handler(HTTPException, http_error_handler)
# 前端传入参数异常处理
application.add_exception_handler(RequestValidationError, http422_error_handler)
# 服务器异常处理
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 路由
application.include_router(AllRouter)

# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 静态资源目录
# application.mount('/resources/static', StaticFiles(directory=settings.STATIC_DIR), name="static")


app = application


def start():
    """
    Launched with `poetry run dev` at root level
    :return: None
    """
    uvicorn.run("src.main:app", port=9090, reload=True)
