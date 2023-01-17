import sqlalchemy as sa

from app.models.modelbase import SqlAlchemyBase


class Submenu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "submenus"

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    dishes_count = sa.Column(sa.Integer)
    menu_id = sa.Column(sa.ForeignKey("menus.id"))

    def __repr__(self):
        return f"<Submenu {self.id}>"
