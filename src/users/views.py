from src.users.schemas import UserPayload, UserResponse
from src.users.models import User
from fastapi import APIRouter
import uuid

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(payload: UserPayload):
    user_created = User(**payload.dict())
    return UserResponse(**user_created.dict())
