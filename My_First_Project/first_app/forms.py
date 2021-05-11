from django import forms
from django.core import validators
from first_app import models

# class user_form (forms.Form):
#
#     # field = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
#     # field = forms.IntegerField(validators=[validators.MaxValueValidator(10),validators.MinValueValidator(5)])
#     # field = forms.IntegerField(validators=[even_or_not])
#     user_email= forms.EmailField()
#     user_vemail= forms.EmailField()
#
#     def clean(self):
#         all_clean_data=super().clean()
#         u_email=all_clean_data['user_email']
#         v_email=all_clean_data['user_vemail']
#
#         if u_email != v_email :
#             raise forms.ValidationError('Field is not match')

class Musician_form(forms.ModelForm):
    class Meta:
        model= models.Musician
        fields= "__all__"
