from django.db import models
from subscription.models.subscription import Subscription

class Transaction(models.Model):
    bill = models.IntegerField()
    amount = models.IntegerField()
    subscription = models.ForeignKey(Subscription)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
