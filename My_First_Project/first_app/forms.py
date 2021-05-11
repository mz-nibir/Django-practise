from django import forms
from django.core import validators

def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError('Please insert a Even Number')

class user_form (forms.Form):

    # field = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    # field = forms.IntegerField(validators=[validators.MaxValueValidator(10),validators.MinValueValidator(5)])
    field = forms.IntegerField(validators=[even_or_not])
