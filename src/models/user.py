from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy_file import FileField, ImageField

from src.database import Base


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    img = Column(ImageField())
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False) 
    rgpd = Column(Boolean, nullable=False)