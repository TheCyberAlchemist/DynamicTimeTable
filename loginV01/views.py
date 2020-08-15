from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from .forms import create_user_form

def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username , password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request,"username or password not correct")
	context = {
	
	}
	return render(request,'login.html',context)

def register(request):
	form = create_user_form()
	if request.method == 'POST':
		form = create_user_form(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,"Account made for " + user)
			return redirect('login')
	context = {'form': form}
	return render(request,'register.html',context)

def home(request):
	context = {
	
	}
	return render(request,'home.html',context)