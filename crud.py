from sqlalchemy.orm import Session
import models
import schemas


# BOOK CRUD

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip=0, limit=10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()


def update_book(db, book_id, book):
    db_book = get_book(db, book_id)

    if not db_book:
        return None

    for key, value in book.dict().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db, book_id):
    book = get_book(db, book_id)

    if not book:
        return None

    db.delete(book)
    db.commit()
    return book


# MEMBER CRUD

def create_member(db, member):
    db_member = models.Member(**member.dict())

    db.add(db_member)
    db.commit()
    db.refresh(db_member)

    return db_member


def get_members(db):
    return db.query(models.Member).all()


def get_member(db, member_id):
    return db.query(models.Member).filter(
        models.Member.id == member_id
    ).first()


def delete_member(db, member_id):
    member = get_member(db, member_id)

    if not member:
        return None

    db.delete(member)
    db.commit()

    return member