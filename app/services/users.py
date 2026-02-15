from app import models
from app.security import hash_password

def create_user(email: str, password: str):
    user = models.User(
        email=email,
        hashed_password=hash_password(password)
    )
    return user
