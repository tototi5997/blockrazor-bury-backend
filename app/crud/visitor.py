from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.visitor import Visitor
from app.schemas.visitor import VisitorCreate
from datetime import date


def get_visitors(db: Session, page: int = 1, page_size: int = 10):
    offset = (page - 1) * page_size
    total = db.query(Visitor).count()
    data = db.query(Visitor).offset(offset).limit(page_size).all()
    return {"total": total, "data": data, "page": page, "page_size": page_size}


def create_visitor(db: Session, visitor: VisitorCreate, ip_address: str):
    today = date.today()
    db_visitor = db.query(Visitor).filter_by(visitor_id=visitor.visitor_id,
                                             date=today).first()

    if db_visitor:
        db_visitor.visit_count += 1
    else:
        db_visitor = Visitor(visitor_id=visitor.visitor_id,
                             ip_address=ip_address,
                             visit_count=1,
                             type=visitor.type,
                             date=today)
        db.add(db_visitor)

    db.commit()
    db.refresh(db_visitor)
    return db_visitor


def find_visitor(db: Session, visitor_id: str):
    return db.query(Visitor).filter_by(visitor_id=visitor_id).first()


def count_visitor_by_type(db: Session, type: str):
    total = db.query(func.sum(
        Visitor.visit_count)).filter_by(type=type).scalar()
    return total or 0


def get_visitor_trands(db: Session):
    rows = db.query(
        Visitor.date, Visitor.type,
        func.sum(Visitor.visit_count).label("visit_count")).group_by(
            Visitor.date, Visitor.type).order_by(Visitor.date).all()
    return rows
