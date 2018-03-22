from django.db import models
from django.utils import timezone

# employee     -> username, password, recoveryAnswer, recoveryEmail, createdOn, lastUpdatedOn, deletedOn
# employeeInfo -> employeeId, firstName, lastName, phoneNumber, createdOn, deletedOn

class Emp(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    recovery_email = models.CharField(max_length=20)
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

class EmployeeInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, default='')
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    deleted_on = models.DateTimeField(blank=True, null=True)

class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'username: {}, password: {}'.format(self.username, self.password)
