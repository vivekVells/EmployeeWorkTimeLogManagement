from django.db import models
from django.utils import timezone

# employee     -> username, password, recoveryAnswer, recoveryEmail, createdOn, lastUpdatedOn, deletedOn
# employeeInfo -> employeeId, firstName, lastName, phoneNumber, createdOn, deletedOn

class Employee(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    '''
    recovery_answer = models.CharField(max_length=50)
    recovery_email = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now())
    last_updated_on = models.DateTimeField()
    deleted_on = models.DateTimeField()
    '''