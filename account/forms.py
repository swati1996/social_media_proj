from django.contrib.auth import get_user_model
# from django.contrib.auth import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomCreationForm(UserCreationForm):

    class meta:
        fields =('username','email','password1','password2')
        model = get_user_model()


    # def __init__(self, *args,**kwargs):
    #     super().__init__(*args,**kwargs)
        # self.fields['username'].label = "Enter Name:"
        # self.fields['email'].label = "Email Address:"

    # form = Usercreateform(UserCreationForm) 

