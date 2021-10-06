import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str = "Jobboard | by Eduardo Paiva"
    PROJECT_VERSION: str = "1.1.0"

    POSTBRES_USER: str = os.getenv("POSTBRES_USER")
    POSTBRES_PASSWORD = os.getenv("POSTBRES_PASSWORD")
    POSTBRES_SERVER: str= os.getenv("POSTBRES_SERVER", "localhost")
    POSTBRES_PORT: str=os.getenv("POSTBRES_PORT", 5432)
    POSTBRES_DB: str=os.getenv("POSTBRES_DB","funceme")

    DATABASE_URL = f"postgresql://{POSTBRES_USER}:{POSTBRES_PASSWORD}@{POSTBRES_SERVER}:{POSTBRES_PORT}/{POSTBRES_DB}"

settings = Settings()