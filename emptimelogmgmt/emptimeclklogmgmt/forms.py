from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(max_length=30,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'username' }))
    password = forms.CharField(max_length=30,
                widget=forms.PasswordInput(attrs={ 'class' : 'form-control', 'placeholder' : 'password'}))

class LogStatus(forms.Form):
    notes = forms.CharField(max_length=50,
                widget=forms.Textarea(attrs={ 'class' : 'form-control', 'placeholder' : 'Notes' }))
                
class RegisterForms(forms.Form):
    username = forms.CharField(max_length=30, 
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Username' }))
    password = forms.CharField(max_length=30,
                widget=forms.PasswordInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Password'}))
    recovery_answer = forms.CharField(max_length=30,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Recovery Answer'}))
    recovery_email = forms.CharField(max_length=30,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Recovery Email'}))
    first_name = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'First Name'}))
    middle_name = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Middle Name'}))
    last_name = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Last Name'}))
    department = forms.CharField(max_length=30,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Department'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'Phone Number'}))
    