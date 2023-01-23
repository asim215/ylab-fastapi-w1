from fastapi import FastAPI
import uvicorn
import os
from app.api.v1.api import api_router
from app.core.config import settings
import app.db.session as db_session
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI(title="YLab-W1")
# Manage all templates
templates = Jinja2Templates("app/templates")

app.include_router(api_router, prefix=settings.API_V1_STR)


def configure_db_sqlite():
    db_file = os.path.join(os.path.dirname(__file__), "db", "app.sqlite")
    db_session.global_init_sqlite(db_file)


def configure_db_pg():
    # AsyncIO
    db_session.global_init_pg(True)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "home/index.html",
        {"request": request},
    )


if __name__ == "__main__":
    # configure_db_sqlite()
    configure_db_pg()
    uvicorn.run("main:app", reload=True)
