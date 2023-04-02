"""
Description: The file containing the base API router, which other routers should be added to.
"""

## -- 3rd Party Imports -- ##

from fastapi import APIRouter, Response

## -- Project Imports -- ##

from app.api.resources.resource1.routes import router as resource1_router

## -- API Router -- ##

api_router = APIRouter()

# Register resource routers here
api_router.include_router(resource1_router, tags=["Resource 1"])

## -- Base Routes -- ##

@api_router.get('/')
async def get_hello(response: Response):

    return {"Hello World": "My API"}