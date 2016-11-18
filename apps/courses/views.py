from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses
from ..logreg.models import User
from django.db.models import Count

def index(request):
	context = {
		"blah" : Courses.objects.all()
	}
	return render(request,'courses/index.html', context)

def create_course(request):
	
	Courses.objects.create(name=request.POST["name"],description=request.POST["description"]) 
	
	return redirect(reverse('my_courses:index'))

def remove(request,id):

	course_to_remove= Courses.objects.get(id=id)
	print(course_to_remove.name)
	if request.method == "GET":
		context = {
			"courses": course_to_remove
			}
		return render(request, 'courses/destroy.html', context)
	course_to_remove.delete()
	return redirect(reverse('my_courses:index'))		

def addusertocourse(request):
	user= User.objects.get(id=request.POST['user_id'])
	course = Courses.objects.get(id=request.POST['course_id'])
	course.users.add(user)
	return redirect(reverse('my_courses:adduser'))

def adduser(request):
	print request.POST
	
	context={
		"users": User.objects.all(),
		"courses":Courses.objects.annotate(students=Count('users__id'))
	}
	
	return render(request, 'courses/users_courses.html', context)