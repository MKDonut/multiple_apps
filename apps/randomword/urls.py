from django.conf.urls import url
from . import views
#import random??


urlpatterns = [
    url(r'^$', views.index, name="index")
]