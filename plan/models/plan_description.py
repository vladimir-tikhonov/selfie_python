from django.db import models

class PlanDescription(models.Model):
    description = models.CharField(max_length=512)

    class Meta:
        db_table = 'plan_description'
