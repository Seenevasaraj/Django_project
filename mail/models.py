from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Home(models.Model):
    user=models.ManyToManyField(User)

    def __str__(self):
    	return user.username
class Email(models.Model):
	Email=models.EmailField(max_length=50,blank=False)
			