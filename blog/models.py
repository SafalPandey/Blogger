import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class post(models.Model):
	def get_user_choices():
		users = User.objects.all()
		user_choice = [(u,u) for u in users]
		return user_choice


	author = models.CharField(max_length=50, choices=get_user_choices())
	title = models.CharField(max_length=100)
	image= models.ImageField(null= True, blank= True, upload_to='images/', height_field=None, width_field=None)
	bodytext = models.TextField()
	timestamp = models.DateTimeField('date published')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s" %(self.id)
