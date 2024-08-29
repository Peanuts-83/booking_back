from fastapi import FastAPI

from .routes.bookings import router as bookings_router
from .database import engine
from .models import db_models
from .middleware.middlewares import PrefixMiddleware

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(PrefixMiddleware)

app.include_router(bookings_router)
