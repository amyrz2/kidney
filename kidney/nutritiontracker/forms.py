from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class PersonalForm(forms.Form):
# 	firstname = forms.CharField(label='firstname', max_length=100,required=True)
# 	lastname = forms.CharField(label='lastname', max_length=100,required=True)
# 	phone = forms.CharField(label='phone', max_length=100,required=False)
# 	birthdate = forms.CharField(label='birthdate', max_length=100,required=True)
# 	gender = forms.CharField(label='gender', max_length=50, required=True)
# 	height = forms.CharField(label='gender', max_length=50, required=True)
# 	weight = forms.CharField(label='gender', max_length=50, required=True)
# 	morbidity = forms.CharField(label='morbidity', max_length=50, required=True)

# class NewUserForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100,required=True)
#     password = forms.CharField(widget=forms.PasswordInput(),required=True)
#     email = forms.CharField(label='Email', max_length=50, required=True)


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=100,required=True)
#     password = forms.CharField(widget=forms.PasswordInput(),required=True)

class APISearch(forms.Form):
    food_item = forms.CharField(label='item', max_length=100,required=True)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


