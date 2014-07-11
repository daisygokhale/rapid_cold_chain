from django.db import models
# Create your models here.

class TimeStampedModel(models.Model):
	
	#The date and time this message was created or modified
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
