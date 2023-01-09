from src.database.dbconfig import mysql_config
from urllib.parse import quote_plus as urlquote
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 拼接数据库连接
default_mysql_config = mysql_config.get('default')
db_url: str = f"mysql+asyncmy://{default_mysql_config.username}:" \
              f"{urlquote(default_mysql_config.password)}@" \
              f"{default_mysql_config.host}:{default_mysql_config.port}/" \
              f"{default_mysql_config.database}"

async_engine = create_async_engine(db_url, echo=True, future=True)

async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False, )

Base = declarative_base()

# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session



async def get_db():
    db: AsyncSession = async_session()
    try:
        yield db
    finally:
        await db.close()
