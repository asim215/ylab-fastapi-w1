import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.models.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory
    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = "sqlite:///" + db_file.strip()
    print(f"Connecting to DB with {conn_str}")

    # echo=False to silience sql commands
    engine = sa.create_engine(conn_str, echo=True)

    factory = orm.sessionmaker(bind=engine)

    # To sqlalchemy know all models to build
    # from app.models.menu import Menu
    # from app.models.submenu import Submenu
    # from app.models.dish import Dish
    import app.models.__all_models

    SqlAlchemyBase.metadata.create_all(engine)
