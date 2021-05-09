from django import forms

class user_form (forms.Form):
    user_name = forms.CharField(label='full name',initial='nibir')

    user_email= forms.EmailField(label='User Email')
