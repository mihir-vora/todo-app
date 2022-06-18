from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=False),
	last_name = forms.CharField(max_length=50, required=False),
	email = forms.EmailField(max_length=300, )


	class Meta:
		model = User

		fields = (
			'username', 
			'first_name', 
			'last_name', 
			'email', 
			'password1', 
			'password2',
			
		)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class' : 'form-group form-control',

		})
		self.fields['first_name'].widget.attrs.update({
			'class' : 'form-group form-control',
			
		})
		self.fields['last_name'].widget.attrs.update({
			'class' : 'form-group form-control',
			
		})
		self.fields['email'].widget.attrs.update({
			'class' : 'form-group form-control',
			
		})
		self.fields['password1'].widget.attrs.update({
			'class' : 'form-group form-control',
			
		})
		self.fields['password2'].widget.attrs.update({
			'class' : 'form-group form-control',
			
		})

		for fieldname in ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			

class UserLoginForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
			'username',
			'password1',
		]

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class' : 'form-group form-control'

		})
		self.fields['password1'].widget.attrs.update({
			'class' : 'form-group form-control'
			
		})

		self.fields['password2'].widget.attrs.update({
			'class' : 'form-group form-control'
			
		})