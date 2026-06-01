from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import models
import schemas
import crud

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_member(
        member: schemas.MemberCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(models.Member).filter(
        models.Member.email == member.email
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Email already exists"
        )

    return crud.create_member(db, member)


@router.get("/")
def view_members(
        db: Session = Depends(get_db)
):
    return crud.get_members(db)


@router.delete("/{member_id}")
def delete_member(
        member_id: int,
        db: Session = Depends(get_db)
):

    member = crud.delete_member(
        db,
        member_id
    )

    if not member:
        raise HTTPException(
            404,
            "Member not found"
        )

    return {"message": "Deleted"}