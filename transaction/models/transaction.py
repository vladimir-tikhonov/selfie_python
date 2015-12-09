from django.db import models

class Transaction(models.Model):
    bill = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
