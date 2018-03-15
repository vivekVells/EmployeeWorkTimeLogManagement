from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
    # return HttpResponse('Welcome to Time Clock\'s Home page')
    loginForm = forms.LoginForms()
    context = { 'form' : loginForm}
    return render(request, 'emptimeclklogmgmt/index.html', context)

def login(request):
    return render(request, 'emptimeclklogmgmt/homepage.html', {})