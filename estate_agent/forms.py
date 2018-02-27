from django import forms

from .models import EstateAgent

class EstateAgentCreateForm(forms.Form):
	name				= forms.CharField()
	address1			= forms.CharField(required=False)
	address2			= forms.CharField(required=False)	
	postcode			= forms.CharField(required=False)

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return name

class EstateAgentCreateFormModel(forms.ModelForm):
	# email		= forms.EmailField()
	class Meta:
		model = EstateAgent
		fields = [
			'name',
			'address1',
			'address2',
			'postcode'
		]

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valid name")
		return name