from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import visitor as visitor_crud
from app.crud import page_view as page_view_crud
from app.schemas.reponse import Reponse
from app.schemas.visitor import VisitorCountOut

router = APIRouter()


@router.get("/count/visitor", response_model=Reponse[VisitorCountOut])
def count_visitor(db: Session = Depends(get_db)):
    blockrazor = visitor_crud.count_visitor_by_type(db, type="blockrazor")
    scutum = visitor_crud.count_visitor_by_type(db, type="scutum")
    count = blockrazor + scutum
    return Reponse(
        data={"blockrazor": blockrazor, "scutum": scutum, "count": count},
        message="成功",
    )


@router.get("/trends/visitor")
def trends_visitor(db: Session = Depends(get_db)):
    rows = visitor_crud.get_visitor_trands(db)
    date_set = set()
    trends = {}
    for row in rows:
        if row.date:
            date_str = row.date.strftime("%Y-%m-%d")
            date_set.add(date_str)
            if date_str not in trends:
                trends[date_str] = {"blockrazor": 0, "scutum": 0}
            trends[date_str][row.type] = row.visit_count

    axis = sorted(list(date_set))
    blockrazor = [trends[date].get("blockrazor", 0) for date in axis]
    scutum = [trends[date].get("scutum", 0) for date in axis]
    return Reponse(
        data={"axis": axis, "blockrazor": blockrazor, "scutum": scutum},
        message="成功",
    )


@router.get("/count/page_view")
def count_page_view(db: Session = Depends(get_db)):
    rows = page_view_crud.count_page_view(db)
    axis = [row.page_url for row in rows]
    count = [row.count for row in rows]
    return Reponse(data={"axis": axis, "count": count}, message="成功")
