from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import models
import schemas

router = APIRouter(
    prefix="/borrow",
    tags=["Borrow System"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def borrow_book(
        data: schemas.BorrowCreate,
        db: Session = Depends(get_db)
):

    book = db.query(models.Book).filter(
        models.Book.id == data.book_id
    ).first()

    if not book:
        raise HTTPException(
            404,
            "Book not found"
        )

    if book.available_copies <= 0:
        raise HTTPException(
            400,
            "No copies available"
        )

    borrow = models.Borrow(
        member_id=data.member_id,
        book_id=data.book_id
    )

    book.available_copies -= 1

    db.add(borrow)
    db.commit()

    return {"message": "Book borrowed"}


@router.put("/return/{borrow_id}")
def return_book(
        borrow_id: int,
        db: Session = Depends(get_db)
):

    borrow = db.query(models.Borrow).filter(
        models.Borrow.id == borrow_id
    ).first()

    if not borrow:
        raise HTTPException(
            404,
            "Record not found"
        )

    if borrow.returned:
        raise HTTPException(
            400,
            "Already returned"
        )

    borrow.returned = True

    book = db.query(models.Book).filter(
        models.Book.id == borrow.book_id
    ).first()

    book.available_copies += 1

    db.commit()

    return {"message": "Book returned"}


@router.get("/")
def borrowed_books(
        db: Session = Depends(get_db)
):
    return db.query(models.Borrow).all()