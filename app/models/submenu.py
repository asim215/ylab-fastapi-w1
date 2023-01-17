import sqlalchemy as sa

from app.models.modelbase import SqlAlchemyBase


class Submenu(SqlAlchemyBase):
    # Set name for table
    __tablename__ = "submenus"

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String, nullable=False, index=True)
    description = sa.Column(sa.String, nullable=True)
    dishes_count = sa.Column(sa.Integer, nullable=False, index=True, default=0)
    menu_id = sa.Column(sa.ForeignKey("menus.id"))

    def __repr__(self):
        return f"<Submenu {self.id}>"
