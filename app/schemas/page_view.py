from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class PageViewOut(BaseModel):
    view_id: int
    ip_address: Optional[str]
    visitor_id: Optional[str]
    page_url: Optional[str]
    page_title: Optional[str]
    entry_time: Optional[datetime]
    exit_time: Optional[datetime]
    stay_time: Optional[int]

    class Config:
        from_attributes = True


class PageViewCreate(BaseModel):
    ip_address: Optional[str] = None
    visitor_id: Optional[str]
    page_url: Optional[str]
    page_title: Optional[str] = None
    entry_time: Optional[datetime] = None
    exit_time: Optional[datetime] = None
    stay_time: Optional[int] = None


class PageViewUpdate(BaseModel):
    ip_address: Optional[str] = None
    visitor_id: Optional[str] = None
    page_url: Optional[str] = None
    page_title: Optional[str] = None
    entry_time: Optional[datetime] = None
    exit_time: Optional[datetime] = None
    stay_time: Optional[int] = None


class PageViewListOut(BaseModel):
    total: int
    page: int
    page_size: int
    data: List[PageViewOut]

    class Config:
        from_attributes = True
