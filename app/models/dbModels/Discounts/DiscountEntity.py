from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, ForeignKey, Float, ARRAY, BigInteger
from sqlalchemy.orm import relationship


class DiscountEntity(EntityDB):
    __tablename__ = 'discounts'

    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=True)
    detail_id = Column(Integer, ForeignKey('details.id'), nullable=True)

    name_discount = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    media_urls = Column(ARRAY(String), nullable=True)
    discount = Column(Float, nullable=False)
    for_user = Column(BigInteger, nullable=True)

    car = relationship("CarEntity", back_populates="discount")
    detail = relationship("DetailEntity", back_populates="discount")

    def __init__(
            self, id=None, car_id=None, detail_id=None, name_discount=None, description=None,
            media_urls=None, discount=None, for_user=None
    ):
        self.id = id
        self.car_id = car_id
        self.detail_id = detail_id
        self.name_discount = name_discount
        self.description = description
        self.media_urls = media_urls
        self.discount = discount
        self.for_user = for_user
    
    def to_dict(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'detail_id': self.detail_id,
            'name_discount': self.name_discount,
            'description': self.description,
            'media_urls': self.media_urls,
            'discount': self.discount,
            'for_user': self.for_user
        }