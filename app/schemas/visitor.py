from pydantic import BaseModel, Field
from typing import List, Optional


class VisitorCreate(BaseModel):
    visitor_id: str = Field(..., description="访客ID")
    type: Optional[str] = None
    # ip_address: str = Field(..., description="IP地址")


class VisitorOut(BaseModel):
    visitor_id: str
    ip_address: str
    visit_count: int

    class Config:
        from_attributes = True


class VisitorListOut(BaseModel):
    total: int
    page: int
    page_size: int
    data: List[VisitorOut]

    class Config:
        from_attributes = True
