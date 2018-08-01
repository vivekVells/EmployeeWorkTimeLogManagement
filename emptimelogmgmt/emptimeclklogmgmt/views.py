# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from . import forms
from . models import Employee, EmployeeInfo, Status, Work, EmployeeAES, EmployeeInfoAES
from . import mailer
import datetime
import pyaes

key = 'kkkkkkkkkkkkkkkk'.encode('UTF-8')

userExistsStatus = False
userRef = ''

def pad(key):
    return key + (16 - len(key) % 10) * '{'


def schedule(request):
    mailer.scheduleMailJob()
    return redirect('index')

def stopschedule(request):
    mailer.stopMailer()
    return redirect('index')

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
            employee = Employee.objects.get(username=(str(userRef)))

            # create a new entry of time log status for the employee
            employee.work_set.create(
                work_status=request.POST['status_drop'],
                notes=request.POST['notes']
            )
            
            employees = Employee.objects.all()
            return redirect('home')
        else:
            employees = Employee.objects.all()
            statuses = Status.objects.all()
            work_statuses = Work.objects.filter(date=datetime.date.today())
            ws_desc = work_statuses.order_by('-time')
            context = {'ws_desc' : ws_desc, 'employees' : employees, 'statuses' : statuses, 'logstatus' : logstatusForm, 'userRef' : userRef}
            return render(request,'emptimeclklogmgmt/homepage.html', context)
    else:
        return HttpResponse('Login again using the link: \'http://127.0.0.1:8000/timeclock/\' ')


def getNewAES():
    newaes = pyaes.AESModeOfOperationCTR(key)
    return newaes

def getBackByteFromString(strhavingbyte):
    if(strhavingbyte != ("[")):
        return strhavingbyte[1:].split("'")[1].encode('UTF-8')
    else:
        return strhavingbyte[1:].split("'")[1].encode('UTF-8')

def register(request):
    registerForm = forms.RegisterForms()
    if request.method == 'POST':
        if registerForm.is_valid:
            newaes = pyaes.AESModeOfOperationCTR(key)
            empObj = EmployeeAES (
                username=getNewAES().encrypt(request.POST['username']),
                password=getNewAES().encrypt(request.POST['password']),
                recovery_answer=getNewAES().encrypt(request.POST['recovery_answer']),
                recovery_email=getNewAES().encrypt(request.POST['recovery_email'])
            )
            empObj.save()

            empInfoObj = EmployeeInfoAES (
                employee=empObj,
                first_name=getNewAES().encrypt(request.POST['first_name']),
                middle_name=getNewAES().encrypt(request.POST['middle_name']),
                department=getNewAES().encrypt(request.POST['department']),
                last_name=getNewAES().encrypt(request.POST['last_name']),
                phone_number=getNewAES().encrypt(request.POST['phone_number'])
            )
            empInfoObj.save()

        return redirect('index')
    else:
        context = {'user' : registerForm}
        return render(request, 'emptimeclklogmgmt/registeruser.html', context)
