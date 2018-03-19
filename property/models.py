from django.conf import settings
from django.db import models

from estate_agent.models import EstateAgent
# Create your models here.
class Property(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	estate_agent 	= models.ForeignKey(EstateAgent)
	location		= models.CharField(max_length=120)
	street_name 	= models.CharField(max_length=120)
	property_type	= models.CharField(max_length=120)
	number_rooms	= models.IntegerField()
	description 	= models.TextField(blank=True, null=True, help_text="Enter details of the property")
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	# images			= models.TextField(blank=True, null=True, help_text="Picture locations")

	class Meta:
		ordering = ['-timestamp', '-updated']
