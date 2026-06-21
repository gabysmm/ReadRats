"""Testes para as rotas de comunidades."""
import os

import pytest
from ninja.testing import TestClient

from api.community.routers import router
from apps.users.models import User

client = TestClient(router)  # simula acesso a rota sem subir servidor

TEST_USER_PASSWORD = os.environ.get("TEST_USER_PASSWORD")


@pytest.fixture
def user(db):
    """Cria um usuário de teste no banco de dados."""
    return User.objects.create_user(
        username="Jude", email="duarte@gmail.com", password=TEST_USER_PASSWORD
    )


def test_create_community(user):
    """Testa a criação de uma comunidade com dados válidos."""
    response = client.post(
        "/",
        json={
            "name": "Príncipe Cruel",
            "description": "Leitura do mês",
            "type_community": "temporary",
        },
        user=user,
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Príncipe Cruel"
    assert response.json()["description"] == "Leitura do mês"
    assert response.json()["type_community"] == "temporary"


def test_create_community_invalidy_type(user):
    """Testa que um tipo de comunidade inválido retorna erro 422."""
    response = client.post(
        "/",
        json={
            "name": "A rainha do nada",
            "description": "Segunda leitura do mês",
            "type_community": "cobra",
        },
        user=user,
    )
    assert response.status_code == 422


def test_crete_community_invalid_auth(user):
    """Testa que criar comunidade sem autenticação retorna erro 401."""
    response = client.post(
        "/",
        json={
            "name": "Principe Cruel",
            "description": "Leitura da triologia",
            "type_community": "continuous",
        },
    )
    assert response.status_code == 401
