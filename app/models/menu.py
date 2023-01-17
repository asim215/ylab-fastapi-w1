import sqlalchemy as sa

# from sqlalchemy.dialects.postgresql import UUID
# import uuid


class Menu:
    # Set name for table
    __tablename__ = "menus"

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    submenus_count = sa.Column(sa.Integer)
    dishes_count = sa.Column(sa.Integer)
    # id: str
    # id = sa.Column(UUID(as_uuid=False), primary_key=True)
    # id = sa.Column(sa.String, primary_key=True, autoincrement=True)
    # title: str
    # description: str
    # submenus_count: int
    # dishes_count: int

    def __repr__(self):
        return f"<Menu {self.id}>"
