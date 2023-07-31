import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .schemas import OperationCreate
from .services import get_operations_by_type, post_specific_operation

router = APIRouter()


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    operations_list = await get_operations_by_type(operation_type=operation_type, session=session)
    return operations_list


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    adding_data_result = await post_specific_operation(new_operation=new_operation, session=session)
    return adding_data_result


@router.get("/long_operation")
@cache(expire=60)
async def long_operation():
    time.sleep(2)
    return "Many-many data that have been calculated over the years"
