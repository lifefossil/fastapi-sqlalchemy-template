import aioredis
from aioredis import Redis
from src.database.dbconfig import redis_config


# async def sys_cache() -> Redis:
#     cache_pool = aioredis.ConnectionPool.from_url(
#         f"redis://{redis_config.get('default').host}:{redis_config.get('default').port}",
#         db=redis_config.get('default').database,
#         encoding=redis_config.get('default').encoding,
#         decode_responses=True
#     )
#     return Redis(connection_pool=cache_pool)


class Cache:
    """
    缓冲操作类
    """

    def __init__(self):
        self.cache_pool = aioredis.ConnectionPool.from_url(
            f"redis://{redis_config.get('default').host}:{redis_config.get('default').port}",
            db=redis_config.get('default').database,
            encoding=redis_config.get('default').encoding,
            password=redis_config.get('default').password,
            decode_responses=True
        )
        self.redis: Redis | None = None

    async def get_redis(self) -> Redis:
        if self.redis:
            return self.redis
        self.redis = await Redis(connection_pool=self.cache_pool)
        return self.redis

    async def close_cache(self):
        if self.redis:
            await self.redis.close()


# 实例化, 实现单例模式
cache = Cache()


async def sys_cache() -> Redis:
    """
    获得系统本地缓存
    :return: Redis
    """
    return await cache.get_redis()

