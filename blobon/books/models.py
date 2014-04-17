from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime

import os

STATUS = (
    ('Se', 'Sent'),
    ('Dr', 'Draft'),
    ('Su', 'Submission'),
    ('Pa', 'Paid'),
)

def get_file_path_receipt(instance, filename):
    ext = filename.split('.')[-1]
    prefix = filename.split('.')[0]
    variable = ('receipt')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

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
        return self.organization_name

class Invoice(models.Model):
    author = models.ForeignKey(User)
    client = models.ForeignKey(Client)
    date_of_issue = models.DateTimeField(auto_now_add = True)
    invoice_number = models.PositiveIntegerField(blank=True)
    terms = models.CharField(max_length=1000)
    sub_notes = models.CharField(max_length=1000, blank=True)
    paid_notes = models.CharField(max_length=1000, blank=True)
    notes = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default="Dr", null=True)
    def __unicode__(self):
        return unicode(self.invoice_number)

 

class Project(models.Model):
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client)
    rate_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.client)

class Tax(models.Model):
    name = models.CharField(max_length=20)
    number = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    compound_tax = models.BooleanField(default=False)
    gouv_number = models.CharField(max_length=100, null=True, blank=True)
    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    rate_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return u'%s -  %s' % (self.name, self.project)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    def __unicode__(self):
        return self.name  
  
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    def __unicode__(self):
        return self.name

class Expense(models.Model):
    author = models.ForeignKey(User)
    vendor = models.ForeignKey(Vendor, null=True, blank=True, default=None)
    client = models.ForeignKey(Client, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, null=True, blank=True, default=None)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add = False)
    receipt = models.FileField(verbose_name=_("receipt"), upload_to=get_file_path_receipt, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return unicode(self.id)

class Time(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True)
    notes = models.CharField(max_length=1000)
    rate_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.PositiveIntegerField(blank=True)
    invoice = models.ForeignKey(Invoice, null=True, blank=True)
    #add taxes
    def __unicode__(self):
        return u'%s -  %s - %s' % (self.task, self.notes, self.id)

class Item(models.Model):
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True)
    client = models.ForeignKey(Client, null=True)
    description = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.client)
