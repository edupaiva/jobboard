from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine   #new
from db.base_class import Base  #new



def create_tables():           #new
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
	create_tables()       
	return app

app = start_application()