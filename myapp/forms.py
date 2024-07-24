from django import forms
from myapp.models import TodoList
from django.contrib.auth.models import User

class TodoListModelForm(forms.ModelForm):
    class Meta:
        model=TodoList
        exclude=("id","created_date","user_object")
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control mb-3"})
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User 
        fields=("username","email","password") 
        widgets={

            "username":forms.TextInput(attrs={"class":"form-control"}),

            "email":forms.EmailInput(attrs={"class":"form-control"}),

            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }    

class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))              