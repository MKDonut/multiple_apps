from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
	
	return render(request, 'logreg/index.html')

def register_user(request):
	res = User.objects.register_user(request.POST)
	if res["added"]:
		request.session['logged_in']=True
		messages.success(request, "Successful Registration! Welcome, {}".format(res["new_user"].first_name))
		return redirect(reverse('my_users:success'))
	else:
		request.session['logged_in']=False
		for error in res["errors"]:
			messages.error(request, error)
		return redirect(reverse('my_users:index'))
def login_user(request):
	print("Something")
	reqs = User.objects.Login_user(request.POST)
	if reqs["checked"]:
		request.session['logged_in']=True
		messages.success(request, "Successful Login! Welcome, {}".format(reqs["logger"].first_name))
		return redirect(reverse('my_users:success'))
	else:
		for error in reqs["errors"]:
			request.session['logged_in']=False
			messages.error(request, error)
		return redirect(reverse('my_users:index'))

def success(request):
	if not request.session['logged_in']:
		return redirect(reverse('my_users:index'))
	return render(request,'logreg/success.html')

def logout(request):
	request.session['logged_in']=False
	return redirect(reverse('my_users:index'))
# Create your views here.
