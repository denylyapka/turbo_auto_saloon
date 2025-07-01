from datetime import datetime

from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


class ReviewEntity(EntityDB):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    part_id = Column(Integer, ForeignKey('details.id'), nullable=False)  # К какой запчасти
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)  # Кто оставил
    rating = Column(Integer, nullable=False)  # Оценка от 1 до 5
    comment = Column(Text, nullable=True)     # Текст отзыва
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата отзыва
    
    # Связи
    details = relationship("DetailEntity", back_populates="reviews")
    users = relationship("UserEntity", back_populates="reviews")


    # Метод для расчета среднего рейтинга (можно сделать как property)
    # @property
    # def avg_rating(self) -> float:
    #     if not self.reviews:
    #         return 0.0
    #     return sum([r.rating for r in self.reviews]) / len(self.reviews)
    
    def __init__(self, id=None, part_id=None, customer_id=None, rating=None, comment=None, created_at=None):
        self.id = id
        self.part_id = part_id
        self.customer_id = customer_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at

    def to_dict(self):
        return {
            'id': self.id,
            'part_id': self.part_id,
            'customer_id': self.customer_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at,
        }
