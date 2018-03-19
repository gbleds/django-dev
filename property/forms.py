from django import forms

from .models import Property

class PropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = [
			'estate_agent',
			'location',
			'street_name',
			'property_type',
			'number_rooms',
			'description'	
		]