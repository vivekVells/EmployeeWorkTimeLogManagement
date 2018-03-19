from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models

def index(request):
    # return HttpResponse('Welcome to Time Clock\'s Home page')
    loginForm = forms.LoginForms()
    context = {'form' : loginForm}
    return render(request, 'emptimeclklogmgmt/index.html', context)

def timeclockindex(request):
    # return HttpResponse('Welcome to Time Clock\'s Home page')
    loginForm = forms.LoginForms()
    context = {'form' : loginForm}
    return render(request, 'emptimeclklogmgmt/index.html', context)

def home(request):
    if request.method == 'POST':
        loginForm = forms.LoginForms()
        if loginForm.is_valid:
            userObj = models.user(username=request.POST['username'], password=request.POST['password'])
            userObj.save()
            context = {'form': userObj}
    return render(request, 'emptimeclklogmgmt/homepage.html', context)

def register(request):
    if request.method == 'POST':
        registerForm = forms.RegisterForms()
        if registerForm.is_valid:
            empObj = models.Employee(
                username=request.POST['username'], 
                password=request.POST['password'], 
                recovery_answer=request.POST['recovery_answer'], 
                recovery_email=request.POST['recovery_email']
            )
            ''' 
            empInfoObj = models.EmployeeInfo( 
                first_name=request.POST['first_name'], 
                middle_name=request.POST['middle_name'], 
                last_name=request.POST['last_name'], 
                phone_number=request.POST['phone_number']
            )
            empObj.save()
            empInfoObj.save()
            '''
            empObj.save()
        return redirect('timeclockindex')
    registerForms = forms.RegisterForms()
    context = {'user' : registerForms}
    return render(request, 'emptimeclklogmgmt/registeruser.html', context)