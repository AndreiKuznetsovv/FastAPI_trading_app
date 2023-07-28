from fastapi import Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.exc import ArgumentError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate


async def get_operations_by_type(operation_type: str, session: AsyncSession = Depends(get_async_session)) -> dict:
    try:
        # default title for get queries is query
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": [dict(r._mapping) for r in result],
            "details": "list of requested operations"}
    except ArgumentError:
        raise HTTPException(status_code=500, detail=
        {
            "status": "error",
            "data": None,
            "details": "an exception occurred on the server during a select operation"
        }
                            )


async def post_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        # default title for post queries is statement (or stmt)
        stmt = insert(operation).values(**new_operation.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": "Given data added successfully"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=
        {
            "status": "error",
            "data": None,
            "details": "some sql exception occurred on the server"
        }
                            )
