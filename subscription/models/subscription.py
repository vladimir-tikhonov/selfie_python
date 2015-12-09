from django.db import models
from plan.models.plan import Plan
from user.models import User
from transaction.models.transaction import Transaction

class Subscription(models.Model):
    status = models.IntegerField(default=0)
    plan = models.ForeignKey(Plan)
    customer = models.ForeignKey(User, related_name='purchased_subscriptions')
    subscribee = models.ForeignKey(User)
    transaction = models.ForeignKey(Transaction)

    class Meta:
        db_table = 'subscription'
