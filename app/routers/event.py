from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import event as event_crud
from app.schemas.reponse import Reponse
from typing import Optional
from app.schemas.event import EventListOut, EventCreate, EventOut
from app.utils.ip import get_client_ip

router = APIRouter()


@router.get("", response_model=Reponse[EventListOut])
def list_event(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    visitor_id: Optional[str] = Query(None, alias="visitor_id"),
    ip_address: Optional[str] = Query(None, alias="ip_address"),
    page_url: Optional[str] = Query(None, alias="page_url"),
):
    events = event_crud.get_events(
        db, page, page_size, visitor_id, ip_address, page_url
    )
    return Reponse(data=events, message="成功")


@router.post("/create", response_model=Reponse[EventOut])
def create_event(event: EventCreate, request: Request, db: Session = Depends(get_db)):
    ip_address = get_client_ip(request)
    event_with_ip = event.model_copy(update={"ip_address": ip_address})
    event_crud.create_event(db, event_with_ip)
    return Reponse(data=None, message="成功")
