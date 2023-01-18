from fastapi import FastAPI
import uvicorn
import os
from app.api.v1.api import api_router
from app.core.config import settings

import app.db.session as db_session
from router1 import router_r1

app = FastAPI(title="YLab-W1")

app.include_router(router_r1)
app.include_router(api_router, prefix=settings.API_V1_STR)


def configure_db_sqlite():
    # working dir
    db_file = os.path.join(os.path.dirname(__file__), "db", "app.sqlite")
    db_session.global_init_sqlite(db_file)


def configure_db_pg():
    # working dir
    # db_file = os.path.join(os.path.dirname(__file__), "db", "app.sqlite")
    db_session.global_init_pg()


@app.get("/")
async def index() -> dict:
    return {"message": "Hello Home page"}


if __name__ == "__main__":
    # configure_db_sqlite()
    configure_db_pg()
    uvicorn.run("main:app", reload=True)
