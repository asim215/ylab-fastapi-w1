from typing import List
from sqlalchemy.orm import Session
from .base import CRUDBase
from app.models.menu import Menu


# class CRUDMenu(CRUDBase):
class CRUDMenu:
    def __init__(self, sess: Session):
        # super.__init__(sess)
        self.sess: Session = sess

    def insert(self, menu: Menu) -> bool:
        try:
            self.sess.add(menu)
            self.sess.commit()
        except Exception:
            return False
        return True

    def get_all(self):
        # return self.sess.query(Menu).all()
        return List(self.sess.query(Menu).all())
        # return "test"
        # return List(self.sess.query(Menu.title.asc()).order_by().all())

    def get(self, id: int):
        # return self.sess.query(Menu).filter(Menu.id == id).one_or_none()
        return self.sess.query(Menu).filter(Menu.id == id).first()

    def update(self, id: int) -> bool:
        try:
            self.sess.query(Menu).filter(Menu.id == id).delete()
            self.sess.commit()
        except Exception:
            return False
        return True

    # delete
