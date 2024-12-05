from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Watch(Base):
    __tablename__ = "watches"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=True)
    image_url = Column(String(255), nullable=True)

    # Relations
    brand = relationship("Brand", back_populates="watches", lazy="joined")
    category = relationship("Category", back_populates="watches", lazy="joined")

class Brand(Base):
    __tablename__ = "brands"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(500), nullable=True)
    
    watches = relationship("Watch", back_populates="brand")

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    
    watches = relationship("Watch", back_populates="category")
