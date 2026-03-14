from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import custom_user,Student

class registration_form(UserCreationForm):
    class Meta:
        model = custom_user
        fields = ['first_name','last_name','email','password1','password2']

class student_form(forms.ModelForm):
    email = forms.EmailField(label='Registered Email', required=True)
    class Meta:
        model = Student
        fields = ['email','profile_pic','department','level_duration']

