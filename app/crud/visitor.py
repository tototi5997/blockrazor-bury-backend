from sqlalchemy.orm import Session
from app.models.visitor import Visitor
from app.schemas.visitor import VisitorCreate


def get_visitors(db: Session, page: int = 1, page_size: int = 10):
    offset = (page - 1) * page_size
    total = db.query(Visitor).count()
    data = db.query(Visitor).offset(offset).limit(page_size).all()
    return {"total": total, "data": data, "page": page, "page_size": page_size}


def create_visitor(db: Session, visitor: VisitorCreate, ip_address: str):
    db_visitor = db.query(Visitor).filter_by(
        visitor_id=visitor.visitor_id).first()

    if db_visitor:
        db_visitor.visit_count += 1
    else:
        db_visitor = Visitor(visitor_id=visitor.visitor_id,
                             ip_address=ip_address,
                             visit_count=1,
                             type=visitor.type)
        db.add(db_visitor)

    db.commit()
    db.refresh(db_visitor)
    return db_visitor


def find_visitor(db: Session, visitor_id: str):
    return db.query(Visitor).filter_by(visitor_id=visitor_id).first()
