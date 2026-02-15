from fastapi import APIRouter
from app.schemas import UserCreate, UserOut
from app.services.users import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    return []

@router.post("/", response_model=UserOut)
def register_user(user: UserCreate):
    return create_user(user.email, user.password)
