import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.models.dish import Dish

# import sqlalchemy.orm as orm

# from fastapi_utils.guid_type import GUID

from sqlalchemy_utils import UUIDType
import uuid

from app.models.modelbase import SqlAlchemyBase


class Submenu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "submenus"

    # id = sa.Column(sa.String, primary_key=True)
    # id = sa.Column(GUID, primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid.uuid4().hex))
    id = sa.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # Must be unique for each menu
    title = sa.Column(sa.String, unique=True, nullable=False, index=True)
    description = sa.Column(sa.String, default="")
    dishes_count = sa.Column(sa.Integer, index=True, default=0)
    # Menu relationship
    menu_id = sa.Column(
        # sa.Integer, sa.ForeignKey("menus.id", ondelete="CASCADE"), index=True
        UUIDType(binary=False),
        sa.ForeignKey("menus.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    menu = relationship("Menu")
    # Dishes relationship
    dishes = relationship(
        "Dish",
        back_populates="submenu",
        order_by=Dish.title.asc(),
        passive_deletes=True,
    )

    def __repr__(self):
        return f"<Submenu {self.id}>"
