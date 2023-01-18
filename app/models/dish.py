import sqlalchemy as sa
from sqlalchemy.orm import relationship

# import sqlalchemy.orm as orm

# from fastapi_utils.guid_type import GUID

# import uuid

from app.models.modelbase import SqlAlchemyBase


class Dish(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "dishes"

    # id = sa.Column(GUID, primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # Must be unique for each submenu
    title = sa.Column(sa.String, unique=True, nullable=False, index=True)
    description = sa.Column(sa.String, default="")
    price = sa.Column(sa.Float, nullable=False, default=0)
    # Submenu relationship
    submenu_id = sa.Column(
        sa.Integer, sa.ForeignKey("submenus.id", ondelete="CASCADE"), index=True
    )
    submenu = relationship("Submenu")
    # submenu = orm.relation("Submenu")

    def __repr__(self):
        return f"<Dish {self.id}>"
