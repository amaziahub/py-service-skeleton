import logging

from fastapi import APIRouter, Depends, HTTPException

from service.dependencies import get_user_service
from service.login.scemas.user import UserResponse, UserCreate
from service.login.user_service import UserService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate,
                  service: UserService = Depends(get_user_service)):
    if service.get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return service.create_user(user)
