from django.shortcuts import render
import datetime
def index(request):
	context = {
	"date":datetime.datetime.now()
	}
	return render(request, 'timedisplay/index.html', context)



# Create your views here.
