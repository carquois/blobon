# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.files.temp import NamedTemporaryFile
import urllib2
from urlparse import urlparse
from django.core.files import File
from cgi import parse_qs

from books.models import Client, Project, Task, Time, Invoice, Tax, Expense, Item
from django.contrib.auth.models import User

@login_required
def invoice(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    client = invoice.client
    times = Time.objects.filter(invoice=invoice)
    taxs = Tax.objects.all()
    items = Item.objects.filter(client=client)
    subtotal_1 = 0
    number_of_hours = 0
    subtotal_2 = 0
    sub_tax1 = 0
    subtotal_3 = 0
    sub_tax2 = 0
    total = 0
    for item in items:
      subtotal_2 = subtotal_2 + item.cost
    for time in times:
      number_of_hours = number_of_hours + time.time
      subtotal_1 = subtotal_1 + (time.time * time.rate_per_hour)
    subtotal = subtotal_1 + subtotal_2
    for tax in taxs:
      if not tax.compound_tax:
        tax1 = tax.rate
        x = (tax1 * subtotal)/100
        sub_tax1 = ("%.2f" % round(x,2))
      else:
        subtotal_3 = subtotal + x
        tax2 = tax.rate
        y = (tax2 * subtotal_3)/100
        sub_tax2 = ("%.2f" % round(y,2))
    z = subtotal_3 + y
    total = ("%.2f" % round(z,2))
    return render_to_response('invoice.html',
                             {'invoice': invoice, 'client': client, 'times': times,'taxs': taxs, 
                              'items': items,'total': total, 'sub_tax2':sub_tax2 ,'sub_tax1':sub_tax1 ,'subtotal': subtotal, 'subtotal_1': subtotal_1, 'subtotal_2': subtotal_2, 'number_of_hours': number_of_hours},
                             context_instance=RequestContext(request))
