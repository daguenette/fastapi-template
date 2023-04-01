from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_DRIVERNAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: str

    class Config:
        env_file = ".env"

settings = Settings()