from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, BigInteger, JSON, DateTime, ARRAY
from sqlalchemy.orm import relationship

class UserEntity(EntityDB):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=True)
    patronymic = Column(String(50), nullable=True)
    datetime_reg = Column(DateTime, nullable=False)
    dateborn = Column(DateTime, nullable=True)
    email = Column(String(100), nullable=False)
    hashed_password = Column(String, nullable=False)

    buy_lists = relationship("UserBuyListsEntity", back_populates="users")
    reviews = relationship("ReviewEntity", back_populates="users")
    buy_lists = relationship("UserBuyListsEntity", back_populates="users")

    def __init__(
            self, id=None, name=None, surname=None,
            patronymic=None, datetime_reg=None, dateborn=None,
            email=None, hashed_password=None
    ):
        self.id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.datetime_reg = datetime_reg
        self.dateborn = dateborn
        self.email = email
        self.hashed_password = hashed_password

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "patronymic": self.patronymic,
            "datetime_reg": self.datetime_reg,
            "dateborn": self.dateborn,
            "email": self.email
        }

    def to_dict_secret(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "patronymic": self.patronymic,
            "datetime_reg": self.datetime_reg,
            "dateborn": self.dateborn,
            "email": self.email,
            "hashed_password": self.hashed_password
        }

