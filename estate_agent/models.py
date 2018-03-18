from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from .validators import validate_location
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.
class EstateAgent(models.Model):
	owner				= models.ForeignKey(User)
	name				= models.CharField(max_length=120)
	address1			= models.CharField(max_length=120, null=True, blank=True)
	address2			= models.CharField(max_length=120, null=True, blank=True, validators=[validate_location])	
	postcode			= models.CharField(max_length=8)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name

	def get_absolute_url(self):
		return reverse('estate_agents:detail', kwargs={'slug': self.slug})

def ea_pre_save_receiver(sender, instance, *args, **kwargs):
	print('saving...')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

# def ea_post_save_receiver(sender, instance, *args, **kwargs):
# 	print('saved')
# 	print(instance.timestamp)

pre_save.connect(ea_pre_save_receiver, sender=EstateAgent)
