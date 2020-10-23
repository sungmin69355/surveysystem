from django import forms

class AccountForm(forms.Form):
    name = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=100)
    checkbox = forms.CharField(max_length=100)