from django.db import models
from posts.models.post import Post
from user.models import User

class Vote(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    value = models.IntegerField()

    class Meta:
        db_table = 'vote'
