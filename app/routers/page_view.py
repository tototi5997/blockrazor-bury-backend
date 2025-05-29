from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import page_view as page_view_crud
from app.schemas.reponse import Reponse
from app.schemas.page_view import (
    PageViewListOut,
    PageViewOut,
    PageViewCreate,
    PageViewUpdate,
)
from typing import Optional
from app.utils.ip import get_client_ip

router = APIRouter()


@router.get("", response_model=Reponse[PageViewListOut])
def list_page_views(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    visitor_id: Optional[str] = Query(None, alias="visitor_id"),
    ip_address: Optional[str] = Query(None, alias="ip_address"),
    page_url: Optional[str] = Query(None, alias="page_url"),
    db: Session = Depends(get_db),
):
    page_views = page_view_crud.get_page_views(
        db, page, page_size, visitor_id, ip_address, page_url
    )
    return Reponse(data=page_views, message="成功")


@router.post("/create", response_model=Reponse[PageViewOut])
def create_page_view(
    page_view: PageViewCreate, request: Request, db: Session = Depends(get_db)
):
    ip_address = get_client_ip(request)
    page_view_with_ip = page_view.model_copy(update={"ip_address": ip_address})
    page_view_crud.create_page_view(db, page_view_with_ip)
    return Reponse(data=None, message="成功")


@router.put("/update/{view_id}", response_model=Reponse[PageViewOut])
def update_page_view(
    view_id: int, page_view: PageViewUpdate, db: Session = Depends(get_db)
):
    page_view = page_view_crud.update_page_view(
        db, page_view_id=view_id, page_view_in=page_view
    )
    if not page_view:
        return Reponse(data=None, message="访客不存在")
    return Reponse(data=page_view, message="成功")
