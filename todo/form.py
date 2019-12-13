
from django import forms


class todoform(forms.Form):
    text=forms.CharField(max_length=50)
