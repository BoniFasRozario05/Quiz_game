from django import forms
from base.models import Person

class PersonForms(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'age', 'details']