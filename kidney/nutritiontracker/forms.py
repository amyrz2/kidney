from django import forms

class NewUserForm(forms.Form):
    f_name = forms.CharField(label='First Name', max_length=100,required=True)
    l_name = forms.CharField(label='Last Name', max_length=100,required=True)
    username = forms.CharField(label='Username', max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.CharField(label='Email', max_length=50, required=True)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)