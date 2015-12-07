from django.db import models
from user.models import User

class Post(models.Model):
    picture = models.FileField(upload_to='pictures/%Y/%m/%d')
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'post'
