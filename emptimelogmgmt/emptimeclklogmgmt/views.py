from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from . import forms
from . models import Employee, EmployeeInfo, Status
import time

userExistsStatus = False
userRef = ''

def logout(request):
    global userExistsStatus, userRef
    userExistsStatus = False
    userRef = ''
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('index')

def delSession(request):
    global userExistsStatus, userRef
    userExistsStatus = False
    userRef = ''
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("Session terminated...")

def login(request):
    try:
        user = Employee.objects.get(username=request.POST['username']) 
        if user.password == request.POST['password']:
            request.session['user_id'] = user.id
            global userExistsStatus, userRef
            userExistsStatus = True
            userRef = request.POST['username']
            return True
        else:
            delSession(request)
            return False   
    except Employee.DoesNotExist:
        delSession(request)
        return False

def index(request):
    if request.method == 'POST':
        loginForm = forms.LoginForms()
        if loginForm.is_valid:
            if login(request):
                return redirect('home')
            else:
                context = {'form' : loginForm, 'message' : 'Username and Password didn\'t match' }
                return render(request, 'emptimeclklogmgmt/index.html', context)
    else:
        delSession(request)
        loginForm = forms.LoginForms()
        context = {'form' : loginForm}
        return render(request, 'emptimeclklogmgmt/index.html', context)

def home(request):
    if userExistsStatus:
        logstatusForm = forms.LogStatus()
        if request.method == 'POST':
            # retrieving the employee from Employee
            employee = Employee.objects.get(username=str(userRef))

            # create a new entry of time log status for the employee
            employee.work_set.create(
                work_status=request.POST['status_of'],
                notes=request.POST['notes']
            )
            
            employees = Employee.objects.all()
            return redirect('home')
        else:
            employees = Employee.objects.all()
            statuses = Status.objects.all()
            context = {'employees' : employees, 'statuses' : statuses, 'logstatus' : logstatusForm, 'userRef' : userRef}
            return render(request,'emptimeclklogmgmt/homepage.html', context)
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/timeclock/\' ')

def register(request):
    registerForm = forms.RegisterForms()
    if request.method == 'POST':
        if registerForm.is_valid:       
            empObj = Employee(
                username=request.POST['username'], 
                password=request.POST['password'], 
                recovery_answer=request.POST['recovery_answer'], 
                recovery_email=request.POST['recovery_email']
            )
            empObj.save()
            empInfoObj = EmployeeInfo( 
                employee=empObj,
                first_name=request.POST['first_name'], 
                middle_name=request.POST['middle_name'], 
                department=request.POST['department'],
                last_name=request.POST['last_name'], 
                phone_number=request.POST['phone_number']
            )
            empInfoObj.save()
        return redirect('index')
    else:
        context = {'user' : registerForm}
        return render(request, 'emptimeclklogmgmt/registeruser.html', context)