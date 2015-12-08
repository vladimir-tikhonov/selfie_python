from django.db import models
from plan.models.plan import Plan
from user.models import User

class Subscription(models.Model):
    status = models.IntegerField(default=0)
    plan = models.ForeignKey(Plan)
    customer = models.ForeignKey(User, related_name='purchased_subscriptions')
    subscribee = models.ForeignKey(User)

    class Meta:
        db_table = 'subscription'
