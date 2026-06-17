"""Schemas de validação para as rotas de usuários."""
from ninja import Schema
from pydantic import EmailStr


class RegisterInput(Schema):
    """Dados necessários para registrar um novo usuário."""

    username: str
    email: EmailStr
    password: str


class RegisterOutput(Schema):
    """Tokens JWT retornados após o registro bem-sucedido."""

    access: str
    refresh: str


class UpdateProfile(Schema):
    """Dados opcionais para atualizar o perfil do usuário."""

    username: str | None = None
    email: EmailStr | None = None
    photo: str | None = None


class ChangePassword(Schema):
    """Dados necessários para alterar a senha do usuário."""

    current_password: str
    new_password: str
