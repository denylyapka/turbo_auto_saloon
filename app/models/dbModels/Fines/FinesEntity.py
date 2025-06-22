from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, BigInteger, JSON, DateTime, Text


class FinesEntity(EntityDB):
    __tablename__ = 'fines'

    id = Column(Integer, primary_key=True, nullable=False)
    name_fine = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    deadline_pay = Column(DateTime(timezone=True), nullable=False)
    datetime_receipt = Column(DateTime(timezone=True), nullable=False)

    def __init__(
        self, id=None, name_fine=None, description=None, price=None, deadline_pay=None, datetime_receipt=None
    ):
        self.id = id
        self.name_fine = name_fine
        self.description = description
        self.price = price
        self.deadline_pay = deadline_pay
        self.datetime_receipt = datetime_receipt
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name_fine": self.name_fine,
            "description": self.description,
            "price": self.price,
            "deadline_pay": self.deadline_pay,
            "datetime_receipt": self.datetime_receipt
        }
