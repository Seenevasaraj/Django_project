from django import forms
from django.contrib.auth.models import User
from mail.models import Home
from django.contrib.auth.forms import UserCreationForm
	

class Userform(UserCreationForm):
	email=forms.EmailField()

	class Meta():		
		model=User
		fields=('first_name','last_name','email',)
		
		
	

	