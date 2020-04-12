from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    reason = models.CharField(max_length=280)
    where = models.CharField(max_length=140)
    when = models.DateField()
    duration = models.IntegerField(default=1)

    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)

    approved = models.BooleanField(default=False)
    approved_updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "{} - {}".format(self.where, self.when)
