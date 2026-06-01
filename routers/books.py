from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas

from database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_book(book: schemas.BookCreate,
             db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@router.get("/")
def view_books(skip: int = 0,
               limit: int = 10,
               db: Session = Depends(get_db)):
    return crud.get_books(db, skip, limit)


@router.get("/{book_id}")
def get_book(book_id: int,
             db: Session = Depends(get_db)):

    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(404, "Book not found")

    return book


@router.put("/{book_id}")
def update_book(book_id: int,
                book: schemas.BookCreate,
                db: Session = Depends(get_db)):

    updated = crud.update_book(db, book_id, book)

    if not updated:
        raise HTTPException(404, "Book not found")

    return updated


@router.delete("/{book_id}")
def delete_book(book_id: int,
                db: Session = Depends(get_db)):

    deleted = crud.delete_book(db, book_id)

    if not deleted:
        raise HTTPException(404, "Book not found")

    return {"message": "Book deleted"}