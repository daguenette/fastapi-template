"""
Description:  The main application entry point, where you define and configure the FastAPI app instance.
"""

## -- 3rd Party Imports -- ##

from fastapi import FastAPI, Response
import uvicorn

## -- Project Imports -- ## 

from app.api.base import api_router
from app.config import settings

## -- Init FastAPI & Add Routes -- ##

app = FastAPI() # To remove /docs use add (docs_url=None, redoc_url=None)
app.include_router(api_router)

## -- Start Server Function -- ##

def start():
    uvicorn.run(app, port=int(settings.API_PORT), log_level="debug")
