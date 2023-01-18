import sqlalchemy as sa

# import sqlalchemy.orm as orm

from fastapi_utils.guid_type import GUID

# import uuid

from app.models.modelbase import SqlAlchemyBase


class Dish(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "dishes"

    id = sa.Column(GUID, primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String, nullable=False, index=True)
    description = sa.Column(sa.String, default="")
    # Float or Str?
    price = sa.Column(sa.Float, nullable=False, default=0)
    submenu_id = sa.Column(GUID, sa.ForeignKey("submenus.id"), index=True)
    # submenu = orm.relation("Submenu")

    def __repr__(self):
        return f"<Dish {self.id}>"
