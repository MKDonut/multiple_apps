from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
	blah = random.randint(0, 10**14)
	print blah
	context = {
		"something": blah
	}
	if "count" not in request.session:
		request.session['count'] = 0
	request.session['count'] += 1
	return render(request, 'randomword/index.html', context)


	