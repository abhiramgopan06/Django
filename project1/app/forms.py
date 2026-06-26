from django import forms
from .models import Course

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' # ['name','course']

class LoginForm(forms.Form):
    username =forms.CharField(max_length=20,label="Username",widget=forms.TextInput(attrs={'placeholder':"Enter username"}))
    password =forms.CharField(max_length=20,label="password",widget=forms.PasswordInput(attrs={'placeholder':"Enter password"}))