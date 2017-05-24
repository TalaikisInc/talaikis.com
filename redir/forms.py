from django import forms
from django.utils.translation import ugettext as T
from django.utils.safestring import mark_safe

from .models import Contacts


class ContactForm(forms.Form):
    name = forms.CharField(max_length=140, label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}))
    message = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'placeholder': 'Your message goes here', 'class': 'form-control'}), required=True, label='Message')
