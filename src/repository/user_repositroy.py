from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.model import UserModel
from src.schema.user import UserCreate


async def create_user(db: AsyncSession, user: UserCreate) -> UserModel:
    user_model = UserModel(**user.dict())
    db.add(user_model)
    await db.commit()
    await db.refresh(user_model)
    return user_model


async def get_user_by_id(db: AsyncSession, user_id: int) -> UserModel:
    stat = select(UserModel).where(UserModel.id == user_id)
    result = await db.scalars(statement=stat)
    return result.one_or_none()
