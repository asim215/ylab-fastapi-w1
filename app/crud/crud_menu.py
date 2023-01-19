from typing import List, Dict, Optional
from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.models.menu import Menu
from app.models.submenu import Submenu
from uuid import UUID


class CRUDMenu:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    async def insert(self, menu: Menu) -> bool:
        try:
            sql = insert(Menu).values(
                id=menu.id,
                title=menu.title,
                description=menu.description,
                # member_id=attendance.member_id,
            )
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)

            # self.sess.add(menu)
            # self.sess.commit()
        except Exception:
            return False
        return True

    async def update(self, id: UUID, details: Dict[str, Optional[str]]) -> bool:
        try:
            # details["title"] = details["title"].strip()
            # if details["description"] is not None:
            #     details["description"] = details["description"].strip()
            sql = update(Menu).where(Menu.id == id).values(**details)
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
        except Exception:
            return False
        return True

    async def delete(self, id: UUID) -> bool:
        try:
            sql = delete(Menu).where(Menu.id == id)
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
        except Exception:
            return False
        return True

    async def get_all(self):
        q = await self.sess.execute(select(Menu))
        return q.scalars().all()

    # Submenus
    async def get_all_submenus(self, id: UUID):
        q = await self.sess.execute(select(Submenu).where(Submenu.menu_id == id))
        return q.scalars().all()

    async def get(self, id: UUID):
        q = await self.sess.execute(select(Menu).where(Menu.id == id))
        # return q.scalars().all()
        return q.scalar()

    # def get_all(self):
    # return self.sess.query(Menu).all()
    # return List(self.sess.query(Menu).all())
    # return "test"
    # return List(self.sess.query(Menu.title.asc()).order_by().all())

    # def get(self, id: int):
    # return self.sess.query(Menu).filter(Menu.id == id).one_or_none()
    # return self.sess.query(Menu).filter(Menu.id == id).first()

    # def update(self, id: int) -> bool:
    #     try:
    #         self.sess.query(Menu).filter(Menu.id == id).delete()
    #         self.sess.commit()
    #     except Exception:
    #         return False
    #     return True

    # delete
