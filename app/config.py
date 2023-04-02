"""
Description: The file containing configurations and settings for the application.
"""

## -- 3rd Party Imports -- ##

from pydantic import BaseSettings

## -- Pydantic Built In Settings Class -- ##

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_DRIVERNAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: str
    API_PORT: str

    class Config:
        env_file = ".env"

settings = Settings()