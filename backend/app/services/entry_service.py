from datetime import datetime
from bson import ObjectId
from app.database import db

# Collection MongoDB
entry_collection = db["entries"]


def create_entry(data: dict):
    entry = {
        "title": data.get("title"),
        "content": data.get("content"),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = entry_collection.insert_one(entry)
    entry["_id"] = str(result.inserted_id)
    return entry


def get_all_entries():
    entries = []
    for entry in entry_collection.find():
        entry["_id"] = str(entry["_id"])
        entries.append(entry)
    return entries


def get_entry_by_id(entry_id: str):
    entry = entry_collection.find_one({"_id": ObjectId(entry_id)})
    if entry:
        entry["_id"] = str(entry["_id"])
    return entry


def update_entry(entry_id: str, data: dict):
    data["updated_at"] = datetime.utcnow()
    entry_collection.update_one(
        {"_id": ObjectId(entry_id)},
        {"$set": data}
    )
    return get_entry_by_id(entry_id)


def delete_entry(entry_id: str):
    result = entry_collection.delete_one({"_id": ObjectId(entry_id)})
    return result.deleted_count > 0
