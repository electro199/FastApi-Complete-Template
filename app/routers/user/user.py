from fastapi import APIRouter, Depends

from app.dependencies import current_active_user
from app.models.user import User
from app.services.user import UserManager, get_user_manager

router = APIRouter(prefix="/api/user")


@router.delete("/me")
async def user_soft_delete(
    user: User = Depends(current_active_user),
    user_manager: UserManager = Depends(get_user_manager),
):
    await user_manager.delete_soft(user)
