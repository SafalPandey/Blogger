import datetime
from django.db import models

from django.utils import timezone
# Create your models here.
class post(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	image= models.ImageField(null= True, blank= True, upload_to='images/', height_field=None, width_field=None)
	bodytext = models.TextField()
	timestamp = models.DateTimeField('date published')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s" %(self.id)
