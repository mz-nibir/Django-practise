from django import forms

class user_form (forms.Form):
    # field = forms.CharField(max_length=15,min_length=5)
    choice= (('','select'),('A','A'),('B','B'),('C','C'))
    field = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)
