from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Visitor(Base):
    __tablename__ = 'visitor'

    visitor_id = Column(String(64), primary_key=True)
    ip_address = Column(String(45), nullable=False)
    visit_count = Column(Integer, default=1)
    type = Column(String(64))
