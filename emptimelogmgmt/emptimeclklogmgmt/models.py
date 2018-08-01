# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from datetime import date

class Emp(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    recovery_email = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, default='')
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Employee(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    recovery_email = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "ID: %d Username: %s Password: %s" % (self.id, self.username, self.password)

class EmployeeAES(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    recovery_answer = models.CharField(max_length=500)
    recovery_email = models.CharField(max_length=500)

class EmployeeInfoAES(models.Model):
    employee = models.ForeignKey('EmployeeAES', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    middle_name = models.CharField(max_length=500, blank=True, default='')
    last_name = models.CharField(max_length=500)
    department = models.CharField(max_length=500, default='')
    phone_number = models.CharField(max_length=500, blank=True, null=True)

class EmployeeInfo(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, default='')
    last_name = models.CharField(max_length=40)
    department = models.CharField(max_length=50, default='')
    phone_number = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "ID: %d First Name: %s Middle Name: %s Last Name: %s Phone Number: %s" % (self.id, self.first_name, self.middle_name, self.last_name, self.phone_number)

class Status(models.Model):
    types = models.CharField(max_length=30)
    
    def __str__(self):
        return "%d %s" % (self.id, self.types)

class Work(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    work_status = models.CharField(max_length=30)
    notes = models.CharField(max_length=100, default='', blank=True)
    time = models.TimeField(default=timezone.localtime)
    date = models.DateField(default=date.today)

    def __str__(self):
        return "ID: %d Work Status: %s Notes: %s Time: %s Date: %s" % (self.id, self.work_status, self.notes, self.time, self.date)

class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'username: {}, password: {}'.format(self.username, self.password)
