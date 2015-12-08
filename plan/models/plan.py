from django.db import models
from plan.models.plan_description import PlanDescription

class Plan(models.Model):
    price = models.IntegerField()
    duration = models.IntegerField()
    plan_description = models.ForeignKey(PlanDescription)

    class Meta:
        db_table = 'plan'
