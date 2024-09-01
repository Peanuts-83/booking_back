from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import db_models
from .middleware.middlewares import PrefixMiddleware

# routers #
from .routes.bookings import router as bookings_router
from .routes.comments import router as comments_router
from .routes.guests import router as guests_router
from .routes.invoices import router as invoices_router
from .routes.rooms import router as rooms_router

db_models.Base.metadata.create_all(bind=engine)

#  front-end source
origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:8080",
    "http://localhost:4200"]

app = FastAPI()
app.add_middleware(PrefixMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

app.include_router(bookings_router)
app.include_router(comments_router)
app.include_router(guests_router)
app.include_router(invoices_router)
app.include_router(rooms_router)
