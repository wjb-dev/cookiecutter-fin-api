from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str   = "{{ cookiecutter.project_slug }}"
    version: str    = "0.1.0"

settings = Settings()
