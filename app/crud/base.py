from typing import List
from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, sess: Session):
        self.sess: Session = sess


# del
