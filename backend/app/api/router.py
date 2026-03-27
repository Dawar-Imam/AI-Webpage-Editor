"""
Main API router module.
Combines and registers all endpoint routers for the FastAPI application.
"""
from fastapi import APIRouter
from app.api.endpoints.demo import demo_router

api_router = APIRouter()

api_router.include_router(demo_router, prefix="/api", tags=["demo"])