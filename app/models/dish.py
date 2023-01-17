import sqlalchemy as sa


class Dish:
    # Set name for table
    __tablename__ = "dishes"

    id = sa.Column(sa.String, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    # Float or Str?
    price = sa.Column(sa.Float)
    submenu_id = sa.Column(sa.ForeignKey("submenus.id"))

    def __repr__(self):
        return f"<Dish {self.id}>"
