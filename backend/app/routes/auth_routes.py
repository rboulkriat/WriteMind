from fastapi import APIRouter, HTTPException
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(data: dict):
    token = login_user(
        email=data.get("email"),
        password=data.get("password")
    )

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return token
