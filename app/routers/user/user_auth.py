from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.config import Config
from app import schemas, models

from app.services.user import UserManager, get_user_manager

config = Config()
router = APIRouter(prefix="/api/auth")


@router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register(
    request: Request,
    user_manager: UserManager = Depends(get_user_manager),
):
    pass

@router.post(path="/login", status_code=status.HTTP_201_CREATED)
async def login(
    request: Request,
    user_manager: UserManager = Depends(get_user_manager),
):
    pass