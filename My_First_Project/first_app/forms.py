from django import forms

class user_form (forms.Form):
    field = forms.CharField(max_length=15,min_length=5)
