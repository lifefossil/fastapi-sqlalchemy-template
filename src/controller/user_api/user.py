
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.mysqldb import get_session
from src.repository.user_repositroy import create_user
from src.schema.user import UserCreate

router = APIRouter()



@router.post('/user', summary="", response_model=UserCreate)
async def create_user_(user: UserCreate, session: AsyncSession = Depends(get_session)):
    u = await create_user(user=user, db=session)
    return u