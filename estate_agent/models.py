from django.db import models

# Create your models here.
class EstateAgent(models.Model):
	name				= models.CharField(max_length=120)
	address1			= models.CharField(max_length=120, null=True, blank=True)
	address2			= models.CharField(max_length=120, null=True, blank=True)	
	postcode			= models.CharField(max_length=8)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name