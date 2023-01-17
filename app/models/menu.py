# TODO: Add index=True
import sqlalchemy as sa

from app.models.modelbase import SqlAlchemyBase

# from sqlalchemy.dialects.postgresql import UUID
# import uuid


class Menu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "menus"

    id = sa.Column(sa.String, primary_key=True)
    # Not allowed to be null
    title = sa.Column(sa.String, nullable=False, index=True)
    # Allowed empty
    description = sa.Column(sa.String, nullable=True)
    # Count, index makes count fast
    submenus_count = sa.Column(sa.Integer, nullable=False, index=True, default=0)
    dishes_count = sa.Column(sa.Integer, nullable=False, index=True, default=0)
    # id: str
    # id = sa.Column(UUID(as_uuid=False), primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, autoincrement=True)
    # title: str
    # description: str
    # submenus_count: int
    # dishes_count: int

    def __repr__(self):
        return f"<Menu {self.id}>"
