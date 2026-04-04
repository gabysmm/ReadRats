from django.db import models

class Community(models.Model):
    TYPE_CHOICES = [
        ('temporary', 'Temporary'),
        ('continuous', 'Continuous')
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='communities')
    create_at = models.DateField(auto_now_add=True)