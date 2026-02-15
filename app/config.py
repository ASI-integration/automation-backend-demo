from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "StayAutomated"
    database_url: str = "postgresql://user:password@localhost:5432/app"

settings = Settings()
