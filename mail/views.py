from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from .models import Email
# Create your views here.
def index(request):
	return render(request,'home.html')
def register(request):
	if request.method =='POST':
		username = request.POST['username']
		email=request.POST['email']
		user=User.objects.create_user(username=email,email=username)
		user.save()
		return render(request,'register.html',{'user':user})
     	
	else:
		return redirect('/')
def Sub(request):
	if request.method=='POST':
		em=request.POST.get('email')
		if em:
			obj=Email.objects.create(Email=email)
			obj.save()
		return render(request,'register.html',{'obj':obj})
	else:
		return redirect('/')