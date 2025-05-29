from sqlalchemy import Column, BigInteger, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PageView(Base):
    __tablename__ = "page_view"

    view_id = Column(BigInteger, primary_key=True, autoincrement=True)
    visitor_id = Column(String(64), index=True)
    ip_address = Column(String(45), index=True)
    page_url = Column(String(255))
    page_title = Column(String(255))
    entry_time = Column(DateTime, index=True)
    exit_time = Column(DateTime)
    stay_time = Column(Integer)  # 秒
