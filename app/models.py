from sqlalchemy import Column, Integer, String, DateTime
from .data"base import Base

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    level = Column(String)
    message = Column(String)
    source = Column(String)