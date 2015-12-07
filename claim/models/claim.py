from django.db import models
from posts.models.post import Post
from user.models import User

class Claim(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    reason = models.CharField(max_length=255)

    class Meta:
        db_table = 'claim'
