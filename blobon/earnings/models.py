from django.db import models

from django.contrib.auth.models import User

class Earning(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add = True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)

