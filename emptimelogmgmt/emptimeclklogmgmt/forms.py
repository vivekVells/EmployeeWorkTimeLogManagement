from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'username' }))
    password = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'password'}))

'''
class Employee(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    recovery_answer = models.CharField(max_length=20)
    recovery_email = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated_on = models.DateTimeField()
    deleted_on = models.DateTimeField()

class EmployeeInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank='True')
    last_name = models.CharField(max_length=40)
    phone_number = models.IntegerField(blank='True')
    created_on = models.DateTimeField()
    deleted_on = models.DateTimeField()
'''
class RegisterForms(forms.Form):
    username = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'username' }))
    password = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'password'}))
    recovery_answer = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Recovery Answer'}))
    recovery_email = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Recovery Email'}))
    first_name = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'First Name'}))
    middle_name = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Middle Name'}))
    last_name = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Last Name'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Phone Number'}))
    
    
