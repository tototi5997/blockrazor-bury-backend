from sqlalchemy import Column, BigInteger, String, DateTime, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'
    event_id = Column(BigInteger, primary_key=True, autoincrement=True)
    visitor_id = Column(String(64))
    ip_address = Column(String(45))
    page_url = Column(String(255))
    event_time = Column(DateTime)
    event_type = Column(Integer)  # click/scroll/submit等
    event_target = Column(String(255))  # 目标元素，如按钮id
    event_value = Column(Text)  # 事件附加信息
