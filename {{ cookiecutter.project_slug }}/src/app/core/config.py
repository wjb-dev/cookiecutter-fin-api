from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field("{{ cookiecutter.project_slug }}", env="SERVICE_NAME")
    description: str = Field("{{ cookiecutter.description }}", env="SERVICE_DESC")
    version: str = Field("0.1.0", env="API_VER")

    class Config:
        env_file = ".env"

settings = Settings()
