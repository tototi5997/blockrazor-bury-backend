from fastapi import FastAPI
from app.routers import visitor
from app.routers import page_view
from app.routers import event
from app.routers import chart

app = FastAPI()

app.include_router(visitor.router, prefix='/api/bury/visitors')

app.include_router(page_view.router, prefix='/api/bury/page-views')

app.include_router(event.router, prefix='/api/bury/events')

app.include_router(chart.router, prefix="/api/bury/charts")
