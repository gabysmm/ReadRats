"""Configuração do app de usuários."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configurações do app de usuários do Django."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
