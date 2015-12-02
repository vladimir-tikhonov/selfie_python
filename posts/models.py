from django.db import models

class Post(models.Model):
    picture = models.FileField(upload_to='pictures/%Y/%m/%d')
