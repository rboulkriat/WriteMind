from fastapi import FastAPI
from app.routes.entry_routes import router as entry_router
from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
app = FastAPI(title="WriteMind API")

app.include_router(entry_router)
app.include_router(user_router)
app.include_router(auth_router)
