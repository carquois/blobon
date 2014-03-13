from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Client(models.Model):
    organization_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    street_adress = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return self.id

class Invoice(models.Model):
    author = models.ForeignKey(User)
    client = models.ForeignKey(Client)
    date_of_issue = models.DateTimeField(auto_now_add = True)
    invoice_number = models.PositiveIntegerField(blank=True)
    terms = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return self.id

class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client)
    rate_per_hour = models.PositiveIntegerField(blank=True)
    def __unicode__(self):
        return self.id


class Tax(models.Model):
    name = models.CharField(max_length=20)
    rate = models.PositiveIntegerField()
    number = models.PositiveIntegerField(blank=True)
    compound_tax = models.BooleanField(default=False)
    def __unicode__(self):
        return self.id

class Expense(models.Model):
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.id

class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    rate_per_hour = models.PositiveIntegerField(blank=True)
    def __unicode__(self):
        return self.id

class Time(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True)
    notes = models.CharField(max_length=1000)
    rate_per_hour = models.PositiveIntegerField(blank=True)
    time = models.PositiveIntegerField(blank=True)
    #add taxes
    def __unicode__(self):
        return self.id

class Item(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True)
    def __unicode__(self):
        return self.id
