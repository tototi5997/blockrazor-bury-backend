from sqlalchemy import Column, String, Integer, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Visitor(Base):
    __tablename__ = "visitor"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    visitor_id = Column(String(64), nullable=False)
    ip_address = Column(String(45), nullable=False)
    visit_count = Column(Integer, default=1)
    type = Column(String(64))
    date = Column(DateTime)
