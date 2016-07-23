# -*- encoding:utf8 -*-
from django import forms

class RegistForm(forms.Form):
    username=forms.CharField(max_length=18)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())



