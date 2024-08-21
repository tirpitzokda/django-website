from django import forms
from clients.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'price', 'quantity']


class UpdateQuantityForm(forms.ModelForm):
	model = Product
	fields = ['quantity']


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group



class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)