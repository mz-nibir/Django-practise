from django import forms

class user_form (forms.Form):
    field = forms.BooleanField(required=False)
