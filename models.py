from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250))
    author = Column(String(255))
    category = Column(String(300))
    available_copies = Column(Integer)


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    email = Column(String(255), unique=True)
    phone = Column(String(100))


class Borrow(Base):
    __tablename__ = "borrow"

    id = Column(Integer, primary_key=True, index=True)

    member_id = Column(Integer, ForeignKey("members.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    returned = Column(Boolean, default=False)

    member = relationship("Member")
    book = relationship("Book")