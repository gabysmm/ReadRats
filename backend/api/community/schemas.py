"""Schemas de validação para as rotas de comunidades."""
from datetime import date
from typing import Literal

from ninja import Schema


class CreateCommunityInput(Schema):
    """Dados necessários para criar uma nova comunidade."""

    name: str
    description: str
    type_community: Literal["temporary", "continuous"]


class UserSummary(Schema):
    """Representação resumida de um usuário para uso em respostas."""

    id: int
    username: str


class CreateCommunityOutput(Schema):
    """Dados retornados após a criação bem-sucedida de uma comunidade."""

    id: int
    name: str
    description: str
    type_community: Literal["temporary", "continuous"]
    create_at: date
    creator: UserSummary
