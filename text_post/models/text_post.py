from django.db import models
from user.models import User

class Post(models.Model):
    content = models.CharField()
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'text_post'
