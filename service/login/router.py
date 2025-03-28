import logging

from fastapi import APIRouter, HTTPException, Depends, status

from service.dependencies import get_user_service
from service.login.auth_utils import create_access_token, verify_password
from service.users.scemas.user import LoginResponse, LoginRequest
from service.users.user_service import UserService

logger = logging.getLogger(__name__)
router = APIRouter()


# Login endpoint
@router.post("", response_model=LoginResponse)
def login(login_request: LoginRequest,
          service: UserService = Depends(get_user_service)):
    user = service.get_user_by_username(login_request.username)

    if user is None or not verify_password(login_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token}
