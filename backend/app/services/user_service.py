from datetime import datetime
from bson import ObjectId
from passlib.context import CryptContext
from app.database import db

# Configuration du hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Collection MongoDB
user_collection = db["users"]


# ---------- UTILITAIRES ----------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ---------- CRUD UTILISATEUR ----------
def create_user(data: dict):
    user = {
        "email": data.get("email"),
        "password": hash_password(data.get("password")),
        "full_name": data.get("full_name"),
        "role": data.get("role", "user"),
        "created_at": datetime.utcnow()
    }
    result = user_collection.insert_one(user)
    user["_id"] = str(result.inserted_id)
    user.pop("password")  # ne jamais retourner le mdp
    return user


def get_user_by_email(email: str):
    user = user_collection.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])
    return user


def get_user_by_id(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        user.pop("password", None)
    return user


def delete_user(user_id: str):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0


def update_user(user_id: str, data: dict):
    update_data = {}

    if "email" in data:
        update_data["email"] = data["email"]

    if "full_name" in data:
        update_data["full_name"] = data["full_name"]

    if "password" in data:
        update_data["password"] = hash_password(data["password"])

    if not update_data:
        return None

    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    return get_user_by_id(user_id)
