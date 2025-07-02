from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, BigInteger, JSON, DateTime, ARRAY
from sqlalchemy.orm import relationship


class BuyListsEntity(EntityDB):
    __tablename__ = 'buy_lists'

    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String(100), nullable=False)
    products = Column(ARRAY(JSON), nullable=False)
    datetime_create = Column(DateTime(timezone=True), nullable=False)
    total_price = Column(Integer, nullable=False)
    total_discount = Column(Integer, nullable=True)

    user_association = relationship("UserBuyListsEntity", back_populates="buy_list")

    def __init__(
        self, id=None, type=None, products=None, datetime_create=None, total_price=None, total_discount=None
    ):
        self.id = id
        self.type = type
        self.products = products
        self.datetime_create = datetime_create
        self.total_price = total_price
        self.total_discount = total_discount
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "products": self.products,
            "datetime_create": self.datetime_create,
            "total_price": self.total_price,
            "total_discount": self.total_discount
        }
