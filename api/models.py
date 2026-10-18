from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)

# class BusinessSchema(Base):
#     __tablename__ = 'business'
#     business_id: str = Column(String(50), primary_key=True)
#     name: str = Column(String(100))
#     address: str = Column(String(120))
#     city: str = Column(String(50))
#     state: str = Column(String(2))
#     postal_code: int = Column(Integer)
#     latitude: float = Column(Double)
#     longitude: float =Field(Double)
#     stars: int = Field(Double)
#     review_count: int = Field(Integer)
#     categories:str = Column(String(120))

# class FoodSchema(Base):
#     __tablename__ = 'food'
#     business_id: str = Column(String(50), primary_key=True)
#     photo_id: str = Column(String(50))
#     caption: str = Column(String(200))
#     food: str = Column(String(75))
