from typing import List
import sqlalchemy as sa
from sqlalchemy.orm import relationship

# import sqlalchemy.orm as orm

# from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from app.models.modelbase import SqlAlchemyBase
from app.models.submenu import Submenu

from sqlalchemy_utils import UUIDType

# from sqlalchemy.dialects.postgresql import UUID
# import uuid
from uuid import uuid4, UUID


class Menu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "menus"

    # id = sa.Column(sa.String, primary_key=True, default=str(uuid.uuid4().hex))
    # id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # id = sa.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    # id = sa.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)

    # id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # id = sa.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    id = sa.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    # id = sa.Column(
    #     UUIDType(binary=False), primary_key=True, default=lambda: uuid.uuid4()
    # )
    # Not allowed to be null
    title = sa.Column(sa.String, unique=True, nullable=False, index=True)
    # Allowed empty
    description = sa.Column(sa.String, nullable=True, default="")
    # Count, index makes count fast
    submenus_count = sa.Column(sa.Integer, index=True, default=0)
    dishes_count = sa.Column(sa.Integer, index=True, default=0)

    # Submenus relationship
    submenus: List[Submenu] = relationship(
        "Submenu",
        back_populates="menu",
        order_by=Submenu.title.asc(),
        passive_deletes=True,
    )

    def __repr__(self):
        return f"<Menu {self.id}>"
