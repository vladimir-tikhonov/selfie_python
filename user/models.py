from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.IntegerField(default=0)
