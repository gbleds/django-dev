from django import forms
from .models import EstateAgent

from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            # 'estate_agent',
            'location',
            'street_name',
            'property_type',
            'number_rooms',
            'description'
        ]

    def __init__(self, user=None, *args, **kwargs):
        # print(kwargs.pop('user'))
        super(PropertyForm, self).__init__(*args, **kwargs)
        # estate_agent = self.fields['estate_agent'].queryset = EstateAgent.objects.filter(user=user)
        # self.initial['estate_agent'] = estate_agent[0]