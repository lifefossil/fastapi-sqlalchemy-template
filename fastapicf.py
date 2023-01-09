import os.path
from pydantic import BaseSettings
from typing import List
from src.core.config import poetry_config
from src.core.constants import PROJECT_ROOT_PATH


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = poetry_config.version
    PROJECT_NAME: str = poetry_config.project_name
    DESCRIPTION: str = poetry_config.description
    # 静态资源目录
    STATIC_DIR: str = str(PROJECT_ROOT_PATH/'resources'/'static')
    # 跨域请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']
    # Session
    SECRET_KEY = "LULULULA"
    SESSION_COOKIE = 'session_id'
    SESSION_MAX_AGE = 14 * 24 * 60 * 60


settings = Config()