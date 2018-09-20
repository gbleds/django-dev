from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

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


	def __str__(self):
		return self.street_name
		
	def get_absolute_url(self):
		return reverse('property:detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-timestamp', '-updated']
