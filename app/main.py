from fastapi import FastAPI
import uvicorn
import os
from app.api.v1.api import api_router
from app.core.config import settings

# from fastapi.responses import HTMLResponse
import app.db.session as db_session

from fastapi.staticfiles import StaticFiles

# from fastapi.templating import Jinja2Templates
from app.views import home

app = FastAPI(title="YLab-W1")


def configure_db_sqlite():
    db_file = os.path.join(os.path.dirname(__file__), "db", "app.sqlite")
    db_session.global_init_sqlite(db_file)


def configure_db_pg():
    db_session.global_init_pg(True)


def configure_routing():
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(home.router)


def configure():
    configure_routing()
    configure_db_pg()


if __name__ == "__main__":
    configure()
    uvicorn.run("main:app", reload=True)
else:
    configure()
