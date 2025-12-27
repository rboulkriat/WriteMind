from fastapi import APIRouter, HTTPException
from app.services.user_service import (
    create_user,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create(data: dict):
    return create_user(data)


@router.get("/{user_id}")
def get(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}")
def update(user_id: str, data: dict):
    user = update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=400, detail="Nothing to update")
    return user


@router.delete("/{user_id}")
def delete(user_id: str):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
