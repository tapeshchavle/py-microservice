from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    # Storing up to 255 characters for the name, indexed for fast lookup
    name = Column(String(255), index=True)
    description = Column(String(255), nullable=True)
