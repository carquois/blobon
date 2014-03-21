from django.db import models

class Invitation(models.Model):
    email = models.EmailField(max_length=50)

