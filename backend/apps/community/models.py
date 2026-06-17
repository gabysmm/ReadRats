"""Models do app de comunidades."""
from django.db import models


class Community(models.Model):
    """Representa uma comunidade de leitura, podendo ser temporária ou contínua."""

    TYPE_CHOICES = [("temporary", "Temporary"), ("continuous", "Continuous")]
    type_community = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, related_name="communities"
    )
    create_at = models.DateField(auto_now_add=True)


class Membership(models.Model):
    """Representa a participação de um usuário em uma comunidade."""

    ROLE_CHOICE = [("admin", "Admin"), ("normal", "Normal")]
    role = models.CharField(max_length=10, choices=ROLE_CHOICE)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="memberships"
    )
    community = models.ForeignKey(
        "Community", on_delete=models.CASCADE, related_name="memberships"
    )
    input_date = models.DateField(auto_now_add=True)
