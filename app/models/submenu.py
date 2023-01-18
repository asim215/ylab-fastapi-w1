import sqlalchemy as sa

# import sqlalchemy.orm as orm

from fastapi_utils.guid_type import GUID

# import uuid

from app.models.modelbase import SqlAlchemyBase


class Submenu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "submenus"

    # id = sa.Column(sa.String, primary_key=True)

    id = sa.Column(GUID, primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4().hex))
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, index=True)
    description = sa.Column(sa.String, default="")
    dishes_count = sa.Column(sa.Integer, index=True, default=0)
    menu_id = sa.Column(GUID, sa.ForeignKey("menus.id"), index=True)
    # menu = orm.relation("Menu")

    def __repr__(self):
        return f"<Submenu {self.id}>"
