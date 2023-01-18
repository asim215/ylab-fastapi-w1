import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.models.modelbase import SqlAlchemyBase
import asyncio

factory = None


def global_init_sqlite(db_file: str):
    global factory
    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = "sqlite:///" + db_file.strip()
    print(f"Connecting to DB with {conn_str}")

    engine = sa.create_engine(conn_str, echo=True)

    factory = sessionmaker(bind=engine)

    # To sqlalchemy know all models to build
    import app.models.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def global_init_pg(drop: bool = False):
    """Asyncio with postgresql"""
    global factory
    if factory:
        return

    conn_str = "postgresql+asyncpg://postgres:admin2255@localhost:5432/ylab_w1"
    print(f"Connecting to DB with {conn_str}")

    engine = create_async_engine(conn_str, future=True, echo=True)

    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    # To sqlalchemy know all models to build
    import app.models.__all_models

    print(type(SqlAlchemyBase))
    print(type(SqlAlchemyBase.metadata))

    # Async with dropCreation
    async def init_models(drop_all: bool):
        async with engine.begin() as conn:
            if drop_all:
                await conn.run_sync(SqlAlchemyBase.metadata.drop_all)
            await conn.run_sync(SqlAlchemyBase.metadata.create_all)

    asyncio.run(init_models(drop))
