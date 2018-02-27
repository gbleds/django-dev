from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_email(value):
	email = value
	if ".edu" in email:
		raise ValidationError("No email addresses ending with .edu allowed")

LOCATIONS = ['Chelmsford', 'Ipswich', 'London', 'Colchester']

def validate_location(value):
	cat = value.capitalize()
	if not value in LOCATIONS and not cat in LOCATIONS:
		raise ValidationError("Not a valid location")