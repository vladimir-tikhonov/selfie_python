from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(
        max_length=254,
        unique=True
    )
    email = models.EmailField()
    is_active = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(default=timezone.now)
    role = models.IntegerField(default=0)
