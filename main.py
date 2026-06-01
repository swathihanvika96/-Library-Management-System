from fastapi import FastAPI
from database import engine
import models

from routers import books
from routers import members
from routers import borrow

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management System"
)

app.include_router(books.router)
app.include_router(members.router)
app.include_router(borrow.router)


@app.get("/")
def home():
    return {
        "message": "Library Management System API"
    }