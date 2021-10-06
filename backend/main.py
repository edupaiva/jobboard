from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine   
from db.base import Base  

def create_tables():           
	Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
	create_tables()
	print("teste")
	return app

app = start_application()