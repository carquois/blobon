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

from books.forms import ReportForm
from books.models import Client, Project, Task, Time, Invoice, Tax, Expense, Item, Report
from django.contrib.auth.models import User

@login_required
def viewexpense(request):
    expenses = Expense.objects.filter(author=request.user).order_by('-date')
    t = 0
    expenses_total = 0
    for expense in expenses:
      t = t + expense.amount
    expenses_total = ("%.2f" % round(t,2))
#Va être à arranger pour d'autre taxes
    tax1 = get_object_or_404(Tax, name="TPS")
    tax2 = get_object_or_404(Tax, name="TVQ")
    tax1_rate = 1 + (tax1.rate/100)
    tax2_rate = 1 + (tax2.rate/100)
    return render_to_response('books/viewexpense.html',
                                {'expenses': expenses,'expenses_total': expenses_total,'tax1_rate': tax1_rate, 'tax2_rate': tax2_rate,},
                                context_instance=RequestContext(request))

@login_required
def viewexpense_year(request, year):
    expenses = Expense.objects.filter(author=request.user).filter(date__year=year).order_by('-date')
    t = 0
    expenses_total = 0
    year = year
#Va être à arranger pour d'autre taxes
    tax1 = get_object_or_404(Tax, name="TPS")
    tax2 = get_object_or_404(Tax, name="TVQ")     
    tax1_rate = 1 + (tax1.rate/100)
    tax2_rate = 1 + (tax2.rate/100)
    for expense in expenses:
      t = t + expense.amount
    expenses_total = ("%.2f" % round(t,2))
    return render_to_response('books/viewexpense.html',
                                {'expenses': expenses,'expenses_total': expenses_total,'year': year,'tax1_rate': tax1_rate, 'tax2_rate': tax2_rate,},
                                context_instance=RequestContext(request))

@login_required
def viewexpense_month(request, year, month):
    expenses = Expense.objects.filter(author=request.user).filter(date__year=year).filter(date__month=month).order_by('-date')
    t = 0
    expenses_total = 0
    month = month
    year = year
#Va être à arranger pour d'autre taxes
    tax1 = get_object_or_404(Tax, name="TPS")
    tax2 = get_object_or_404(Tax, name="TVQ")     
    tax1_rate = 1 + (tax1.rate/100)
    tax2_rate = 1 + (tax2.rate/100)
    for expense in expenses:
      t = t + expense.amount
    expenses_total = ("%.2f" % round(t,2))
    return render_to_response('books/viewexpense.html',
                                {'expenses': expenses,'expenses_total': expenses_total,'year': year,'month': month,'tax1_rate': tax1_rate, 'tax2_rate': tax2_rate,},
                                context_instance=RequestContext(request))

@login_required
def viewexpense_day(request, year, month, day):
    expenses = Expense.objects.filter(author=request.user).filter(date__year=year).filter(date__month=month).filter(date__day=day).order_by('-date')
    t = 0
    expenses_total = 0
    day = day
    month = month
    year = year
#Va être à arranger pour d'autre taxes
    tax1 = get_object_or_404(Tax, name="TPS")
    tax2 = get_object_or_404(Tax, name="TVQ")     
    tax1_rate = 1 + (tax1.rate/100)
    tax2_rate = 1 + (tax2.rate/100)
    for expense in expenses:
      t = t + expense.amount
    expenses_total = ("%.2f" % round(t,2))
    return render_to_response('books/viewexpense.html',
                                {'expenses': expenses,'expenses_total': expenses_total,'year': year,'month': month, 'day': day,'tax1_rate': tax1_rate, 'tax2_rate': tax2_rate,},
                                context_instance=RequestContext(request))




@login_required
def invoice(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    if request.user == invoice.author:
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
      if invoice.with_items:
        for item in items:
          subtotal_2 = subtotal_2 + item.cost
      for time in times:
        number_of_hours = number_of_hours + time.time
        subtotal_1 = subtotal_1 + (time.time * time.rate_per_hour)
      subtotal = subtotal_1 + subtotal_2
      if invoice.with_taxes:
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
      else:
        z = subtotal
      total = ("%.2f" % round(z,2))
      return render_to_response('books/invoice.html',
                               {'invoice': invoice, 'client': client, 'times': times,'taxs': taxs, 
                                'items': items,'total': total, 'sub_tax2':sub_tax2 ,'sub_tax1':sub_tax1 ,'subtotal': subtotal, 'subtotal_1': subtotal_1, 'subtotal_2': subtotal_2, 'number_of_hours': number_of_hours},
                               context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('blogs.views.index'))


@login_required
def newreport(request):
    if request.method == 'POST':
      form = ReportForm(request.POST)
      if form.is_valid():
        report = form.save(commit=False)
        report.author = request.user
        report.save()
        return HttpResponseRedirect(reverse('books.views.viewreport', args=(report.id,)))
      else:
        messages.add_message(request, messages.INFO, _(u"An error has occur please try again"))
        return HttpResponseRedirect(reverse('books.views.newreport'))
    else:
      form = ReportForm()
      return render_to_response('books/newreport.html',
                                {'form': form},
                                context_instance=RequestContext(request))

 
@login_required
def viewreport(request, id):
    report = get_object_or_404(Report, id=id)
    if request.user == report.author:
      if report.client:
        invoices = Invoice.objects.filter(author=request.user).filter(date_of_issue__range=[report.start_date, report.end_date]).filter(status="Pa").filter(client=report.client).order_by('date_of_issue')
      else:
        invoices = Invoice.objects.filter(author=request.user).filter(date_of_issue__range=[report.start_date, report.end_date]).filter(status="Pa").order_by('date_of_issue')
      tax1 = get_object_or_404(Tax, name="TPS")
      tax2 = get_object_or_404(Tax, name="TVQ")
      tax1_rate = 1 + (tax1.rate/100)
      tax2_rate = 1 + (tax2.rate/100)
      taxable_expense_total = 0
      x = 0
      z = 0
      for invoice in invoices:
        tot = 0
        tot2 = 0
        if invoice.with_items:
          for item in invoice.client.item_set.all():
            tot +=  item.cost * item.quantity
        for time in Time.objects.filter(invoice=invoice):
          tot2 += time.rate_per_hour * time.time
        if invoice.with_taxes:
          sub_tot = (tot + tot2) * tax1_rate
          invoice.total = sub_tot * tax2_rate
        else:
          invoice.total = tot + tot2
        if invoice.with_taxes:
          z += invoice.total
        x += invoice.total
      if report.client:
        expenses = Expense.objects.filter(author=request.user).filter(date__range=[report.start_date, report.end_date]).filter(client=report.client).order_by('date')
      else:
        expenses = Expense.objects.filter(author=request.user).filter(date__range=[report.start_date, report.end_date]).order_by('date')
      t = 0
      expenses_total = 0
      taxed_expenses = Expense.objects.filter(author=request.user).filter(taxes__isnull=False).filter(date__range=[report.start_date, report.end_date]).order_by('date').distinct()
      for expense in expenses:
        t = t + expense.amount
      expenses_total = ("%.2f" % round(t,2))
      for expense in taxed_expenses:
        taxable_expense_total = taxable_expense_total + expense.amount
      taxable_expense_total_before = taxable_expense_total/tax2_rate
      tax2_total = (taxable_expense_total)-(taxable_expense_total_before)
      tax1_total =  (taxable_expense_total_before)-(taxable_expense_total_before/tax1_rate)
      return render_to_response('books/report.html',
                                 {'z':z, 'x':x,'invoices': invoices, 'taxable_expense_total': taxable_expense_total, 'expenses': expenses, 'report': report, 'expenses_total': expenses_total,'tax1_rate': tax1_rate, 'tax2_rate': tax2_rate,'tax1': tax1, 'tax2': tax2,'tax1_total': tax1_total,'tax2_total': tax2_total,},
                                  context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect(reverse('books.views.newreport'))
