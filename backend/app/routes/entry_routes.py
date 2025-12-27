from fastapi import APIRouter, HTTPException
from app.services.entry_service import (
    create_entry,
    get_all_entries,
    get_entry_by_id,
    update_entry,
    delete_entry
)

router = APIRouter(
    prefix="/entries",
    tags=["Entries"]
)


@router.post("/")
def create(data: dict):
    return create_entry(data)


@router.get("/")
def get_all():
    return get_all_entries()


@router.get("/{entry_id}")
def get_one(entry_id: str):
    entry = get_entry_by_id(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


@router.put("/{entry_id}")
def update(entry_id: str, data: dict):
    return update_entry(entry_id, data)


@router.delete("/{entry_id}")
def delete(entry_id: str):
    if not delete_entry(entry_id):
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"message": "Entry deleted"}
