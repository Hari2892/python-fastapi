from pydantic import BaseModel, EmailStr, validator
from datetime import datetime


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UserUpdatePassword(BaseModel):
    password: str | None = None

    @validator("password")
    def validate_password(cls, value):
        if value is None or value.strip() == "":
            raise ValueError("Password Field is required")
        return value


class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True