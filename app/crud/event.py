from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate


def get_events(db: Session,
               page: int = 0,
               page_size: int = 10,
               visitor_id=None,
               ip_address=None,
               page_url=None):
    offset = (page - 1) * page_size
    query = db.query(Event)
    if visitor_id:
        query = query.filter(Event.visitor_id == visitor_id)
    if ip_address:
        query = query.filter(Event.ip_address == ip_address)
    if page_url:
        query = query.filter(Event.page_url == page_url)
    total = query.count()
    data = query.offset(offset).limit(page_size).all()
    return {"total": total, "data": data, "page": page, "page_size": page_size}


def create_event(db: Session, event_in: EventCreate):
    db_event = Event(**event_in.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
