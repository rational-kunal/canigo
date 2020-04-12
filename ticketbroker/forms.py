import datetime

from django import forms
from django.core.exceptions import ValidationError


class TicketCreationForm(forms.Form):
    reason = forms.CharField(max_length=280, widget=forms.Textarea)
    where = forms.CharField(max_length=140)
    when = forms.DateField(widget=forms.DateInput, initial=datetime.date.today)
    duration = forms.IntegerField(initial=1)
