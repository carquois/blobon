from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField, ImageField, ModelMultipleChoiceField, EmailField
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField, BooleanField
from django.db import models

from books.models import Report

class ReportForm(ModelForm):
    start_date = DateField(required=True, widget=forms.TextInput(attrs={'class':'datepicker form-control'}))
    end_date = DateField(required=True, widget=forms.TextInput(attrs={'class':'datepicker form-control'}))
    invoice = BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':''}))
    expense = BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':''}))
    taxes = BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':''}))
    timesheet = BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':''}))
    class Meta:
        model = Report
        fields = ('start_date', 'end_date', 'invoice', 'expense', 'taxes', 'timesheet', )
