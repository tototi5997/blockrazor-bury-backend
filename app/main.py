from fastapi import FastAPI
from app.routers import visitor
from app.routers import page_view
from app.routers import event

app = FastAPI()

app.include_router(visitor.router, prefix='/visitors')

app.include_router(page_view.router, prefix='/page-views')

app.include_router(event.router, prefix='/events')
