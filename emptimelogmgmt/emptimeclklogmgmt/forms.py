from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'username' }))
    password = forms.CharField(max_length=20,
                widget=forms.TextInput(attrs={ 'class' : 'form-control', 'placeholder' : 'password'}))