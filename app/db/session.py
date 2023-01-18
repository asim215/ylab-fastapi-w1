import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
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

    # echo=False to silience sql commands
    engine = sa.create_engine(conn_str, echo=True)

    factory = sessionmaker(bind=engine)

    # To sqlalchemy know all models to build
    # from app.models.menu import Menu
    # from app.models.submenu import Submenu
    # from app.models.dish import Dish
    import app.models.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def global_init_pg():
    global factory
    if factory:
        return

    # if not db_file or not db_file.strip():
    #     raise Exception("You must specify a db file.")
    # conn_str = "postgresql://postgres:admin2255@localhost:5432/ylab_w1"
    conn_str = "postgresql+asyncpg://postgres:admin2255@localhost:5432/ylab_w1"
    print(f"Connecting to DB with {conn_str}")

    # echo=False to silience sql commands
    # engine = sa.create_engine(conn_str, echo=True)
    engine = create_async_engine(conn_str, future=True, echo=True)

    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

    # To sqlalchemy know all models to build
    # from app.models.menu import Menu
    # from app.models.submenu import Submenu
    # from app.models.dish import Dish
    import app.models.__all_models

    print(type(SqlAlchemyBase))
    print(type(SqlAlchemyBase.metadata))
    # SqlAlchemyBase.metadata.create_all(engine)

    async def init_models():
        async with engine.begin() as conn:
            await conn.run_sync(SqlAlchemyBase.metadata.drop_all)
            await conn.run_sync(SqlAlchemyBase.metadata.create_all)

    asyncio.run(init_models())
