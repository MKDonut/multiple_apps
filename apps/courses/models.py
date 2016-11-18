from __future__ import unicode_literals
from ..logreg.models import User
from django.db import models

class Courses(models.Model):
	name = models.CharField(max_length= 255)
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	users= models.ManyToManyField(User, related_name="courses")

# Create your models here.
