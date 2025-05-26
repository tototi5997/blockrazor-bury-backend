from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class EventBase(BaseModel):
    visitor_id: Optional[str]
    ip_address: Optional[str] = None
    page_url: Optional[str] = None
    event_time: Optional[datetime] = None
    event_type: Optional[int] = None
    event_target: Optional[str] = None
    event_value: Optional[str] = None


class EventCreate(EventBase):
    pass


class EventOut(EventBase):
    event_id: int


class EventListOut(BaseModel):
    total: int
    page: int
    page_size: int
    data: List[EventOut]

    class Config:
        from_attributes = True
