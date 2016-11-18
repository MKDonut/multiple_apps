from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
	return render(request,'survey/index.html')

def process(request):
	count = 0
	if 'count' not in request.session:
		request.session['count']= 0
	request.session['count'] += 1 
	
	request.session["name"] = request.POST["name"]
	request.session["location"] = request.POST["location"]
	request.session["language"] = request.POST["language"]
	request.session["comments"] = request.POST["comments"]
	
	return redirect(reverse('my_survey:result'))

def result(request):
	return render(request, 'survey/result.html')

def reset(request):
	return redirect(reverse('my_survey:index'))
