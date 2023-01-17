import sqlalchemy as sa


class Submenu:
    # Set name for table
    __tablename__ = "submenus"

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    dishes_count = sa.Column(sa.Integer)
    menu_id = sa.Column(sa.ForeignKey("menus.id"))

    def __repr__(self):
        return f"<Submenu {self.id}>"
