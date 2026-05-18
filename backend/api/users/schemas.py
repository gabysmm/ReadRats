from ninja import Schema
from pydantic import EmailStr


class RegisterInput(Schema):
    username: str
    email: EmailStr
    password: str


class RegisterOutput(Schema):
    access: str
    refresh: str


class UpdateProfile(Schema):
    username: str | None = None
    email: EmailStr | None = None
    photo: str | None = None


class ChangePassword(Schema):
    current_password: str
    new_password: str
