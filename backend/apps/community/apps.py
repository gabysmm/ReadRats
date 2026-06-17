"""Configuração do app de comunidades."""
from django.apps import AppConfig


class CommunityConfig(AppConfig):
    """Configurações do app de comunidades do Django."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.community"
