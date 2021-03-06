from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):

    form_class = forms.CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
