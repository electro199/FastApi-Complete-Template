from fastapi import Depends, HTTPException, Query
from app.database import get_db_session, AsyncSession
from app.utils import HttpClient
from app import models
from sqlalchemy import select


async def current_user(
    user_id: int = Query(..., description="User ID"),
    db_session: AsyncSession = Depends(get_db_session),
) -> models.User:
    """
    Ensure that the user exists in the database.
    """
    result = await db_session.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")

    return user

http_client = HttpClient()
