import datetime

from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, ForeignKey, Integer, BigInteger, DateTime
from sqlalchemy.orm import relationship


class WatchListEntity(EntityDB):
    __tablename__ = 'watch_lists'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)  # Ссылка на таблицу users
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=True)
    detail_id = Column(Integer, ForeignKey('details.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Определение отношений
    user = relationship("UserEntity", back_populates="watch_list")
    car = relationship("CarEntity", back_populates="watch_lists")  # Должно соответствовать CarEntity
    detail = relationship("DetailEntity", back_populates="watch_list")  # Должно совпадать с DetailEntity


    def __init__(
            self, id=None, user_id=None, car_id=None, detail_id=None, created_at=None
    ):
        self.id = id
        self.user_id = user_id
        self.car_id = car_id
        self.detail_id = detail_id
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'car_id': self.car_id,
            'detail_id': self.detail_id,
            'created_at': self.created_at
        }
