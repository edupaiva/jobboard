import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "Jobboard | by Eduardo Paiva"
    PROJECT_VERSION: str = "1.1.0"

    POSTRES_USER: str = os.getenv("POSTGRES_USER")
    POSTBRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTBRES_SERVER: str= os.getenv("POSTGRES_SERVER", "localhost")
    POSTBRES_PORT: str=os.getenv("POSTGRES_PORT", 5432)
    POSTBRES_DB: str=os.getenv("POSTGRES_DB","funceme")
    DATABASE_URL = f"postgresql://{POSTRES_USER}:{POSTBRES_PASSWORD}@{POSTBRES_SERVER}:{POSTBRES_PORT}/{POSTBRES_DB}"

settings = Settings()