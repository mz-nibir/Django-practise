from django import forms

class user_form (forms.Form):
    user_name = forms.CharField(label='full name',widget=forms.TextInput(attrs={'placeholder':'please write your name','style':'width:300px'}))

    user_email= forms.EmailField(label='User Email')

    dob = forms.DateField(label='Date of Birth', widget=forms.TextInput(attrs={'type':'date'}))
