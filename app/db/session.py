import sqlalchemy as sa
import sqlalchemy.orm as orm

factory = None


def global_init(db_file: str):
    global factory
    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = "sqlite:///" + db_file.strip()
    # echo=False to silience sql commands
    engine = sa.create_engine(conn_str, echo=True)

    factory = orm.sesessionmaker(bind=engine)
