from sqlalchemy.orm import Session
from app.models.page_view import PageView
from app.schemas.page_view import PageViewCreate, PageViewUpdate


def get_page_views(db: Session,
                   page: int = 0,
                   page_size: int = 100,
                   visitor_id=None,
                   ip_address=None,
                   page_url=None):
    offset = (page - 1) * page_size
    query = db.query(PageView)
    if visitor_id:
        query = query.filter(PageView.visitor_id == visitor_id)
    if ip_address:
        query = query.filter(PageView.ip_address == ip_address)
    if page_url:
        query = query.filter(PageView.page_url == page_url)
    total = query.count()
    data = query.offset(offset).limit(page_size).all()
    return {"total": total, "data": data, "page": page, "page_size": page_size}


def create_page_view(db: Session, page_view_in: PageViewCreate):
    db_page_view = PageView(**page_view_in.model_dump())
    db.add(db_page_view)
    db.commit()
    db.refresh(db_page_view)
    return db_page_view


def update_page_view(db: Session, page_view_id: int,
                     page_view_in: PageViewUpdate):
    db_page_view = db.query(PageView).filter(
        PageView.view_id == page_view_id).first()

    if not db_page_view:
        return None

    update_data = page_view_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_page_view, key, value)

    db.commit()
    db.refresh(db_page_view)
    return db_page_view
