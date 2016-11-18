from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^create_course$', views.create_course, name="create_course"),
    url(r'^(?P<id>\d+)/remove$', views.remove, name="remove"),
    url(r'^addusertocourse$', views.addusertocourse, name="users_courses"),
    url(r'^adduser$', views.adduser, name="adduser")
]

