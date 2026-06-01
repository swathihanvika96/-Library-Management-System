from pydantic import BaseModel, EmailStr, Field


# BOOK

class BookBase(BaseModel):
    title: str
    author: str
    category: str
    available_copies: int


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True


# MEMBER

class MemberBase(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(min_length=10, max_length=10)


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    id: int

    class Config:
        from_attributes = True


# BORROW

class BorrowCreate(BaseModel):
    member_id: int
    book_id: int


class BorrowResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    returned: bool

    class Config:
        from_attributes = True