from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.schemas.visitor import VisitorOut, VisitorCreate, VisitorListOut
from app.db.session import get_db
from app.crud import visitor as visitor_crud
from app.schemas.reponse import Reponse
from app.utils.ip import get_client_ip

router = APIRouter()


@router.get('', response_model=Reponse[VisitorListOut])
def list_visitors(page: int = Query(1, ge=1),
                  page_size: int = Query(10, ge=1, le=100),
                  db: Session = Depends(get_db)):
    visitors = visitor_crud.get_visitors(db, page, page_size)
    return Reponse(data=visitors, message='成功')


@router.post('/create', response_model=Reponse[VisitorOut])
def create_visitor(visitor: VisitorCreate,
                   request: Request,
                   db: Session = Depends(get_db)):
    ip_address = get_client_ip(request)
    visitor = visitor_crud.create_visitor(db, visitor, ip_address)
    return Reponse(data=None, message='成功')


@router.get('/{visitor_id}', response_model=Reponse[VisitorOut])
def find_visitor(visitor_id: str, db: Session = Depends(get_db)):
    visitor = visitor_crud.find_visitor(db, visitor_id)
    if not visitor:
        return Reponse(data=None, message='访客不存在')
    return Reponse(data=visitor, message='成功')
