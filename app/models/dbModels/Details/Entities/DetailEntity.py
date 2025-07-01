from datetime import datetime

from app.models.dbModels.EntityDB import EntityDB
from sqlalchemy import Column, String, Integer, Float, JSON, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship



class DetailEntity(EntityDB):
    __tablename__ = 'details'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    part_number = Column(String(100), nullable=False, index=True)
    oem_number = Column(String(100), nullable=True)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    weight_kg = Column(Float, nullable=True)
    description = Column(Text, nullable=True)
    image_urls = Column(JSON, nullable=True)  # Список ссылок: ["img1.jpg", "img2.jpg"]
    warranty_months = Column(Integer, nullable=True)
    installation_guide_url = Column(String(255), nullable=True)
    video_review_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    brand = relationship("Brand", back_populates="details")
    category = relationship("Category", back_populates="details")
    cross_references = relationship("CrossReference", back_populates="details")
    compatibilities = relationship("Compatibility", back_populates="details")
    reviews = relationship("Review", back_populates="details")

    def __init__(
            self, id=None, name=None, part_number=None, oem_number=None, brand_id=None, category_id=None, price=None,
            quantity=None, weight_kg=None, description=None, image_urls=None, warranty_months=None,
            installation_guide_url=None, video_review_url=None, created_at=None
    ):
        self.id = id
        self.name = name
        self.part_number = part_number
        self.oem_number = oem_number
        self.brand_id = brand_id
        self.category_id = category_id
        self.price = price
        self.quantity = quantity
        self.weight_kg = weight_kg
        self.description = description
        self.image_urls = image_urls
        self.warranty_months = warranty_months
        self.installation_guide_url = installation_guide_url
        self.video_review_url = video_review_url
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'part_number': self.part_number,
            'oem_number': self.oem_number,
            'brand_id': self.brand_id,
            'category_id': self.category_id,
            'price': self.price,
            'quantity': self.quantity,
            'weight_kg': self.weight_kg,
            'description': self.description,
            'image_urls': self.image_urls,
            'warranty_months': self.warranty_months,
            'installation_guide_url': self.installation_guide_url,
            'video_review_url': self.video_review_url,
            'created_at': self.created_at,
        }
