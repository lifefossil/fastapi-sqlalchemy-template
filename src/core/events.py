# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: fastapi事件监听
"""

from typing import Callable
from fastapi import FastAPI
from src.database.redisdb import cache


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        # APP启动完成后触发
        print("启动完毕")
        app.state.cache = await cache.get_redis()

    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """

    async def stop_app() -> None:
        # APP停止时触发
        print("停止")
        await cache.close_cache()

    return stop_app
