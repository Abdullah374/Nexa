from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CollegeSearchform(forms.Form):
    institute_name = forms.CharField(required=False, max_length=255)
    city = forms.CharField(required=False, max_length=100, label='City')
    state = forms.CharField(required=False, max_length=100, label='State')
    course = forms.CharField(required=False, max_length=100, label='Course')
    govt = forms.BooleanField(required=False, label='Government Institution')

