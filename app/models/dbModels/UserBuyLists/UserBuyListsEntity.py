from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import relationship


class UserBuyListsEntity(EntityDB):
    __tablename__ = 'user_buy_lists'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)  # Ссылка на таблицу users
    buy_list_id = Column(Integer, ForeignKey('buy_lists.id'), nullable=False)  # Ссылка на таблицу buy_lists

    # Определение отношений
    user = relationship("UserEntity", back_populates="buy_lists")
    buy_list = relationship("BuyListsEntity", back_populates="user_associations")


    def __init__(
            self, id=None, user_id=None, buy_list_id=None
    ):
        self.id = id
        self.user_id = user_id
        self.buy_list_idid = buy_list_id


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "buy_list_id": self.buy_list_id
        }
