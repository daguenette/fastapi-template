from fastapi import APIRouter
from app.api.ressources.taxes.routes import router as taxes_routes


api_router = APIRouter()

# Register resource routers here
api_router.include_router(taxes_routes, tags=["Taxes"])