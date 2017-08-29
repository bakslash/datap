from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
	data_collector=models.CharField(max_length=50)
	name =models.CharField(max_length=50, unique=True)
	date_collected = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=50)
	favourite_drink = models.CharField(max_length=20)
	date_added = models.DateTimeField(default=timezone.now)

def __str__(self):
	return self.name

	
		