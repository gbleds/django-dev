from django.db import models
from estate_agent.models import EstateAgent
from django.contrib.auth.models import(
	AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("Users must have a password")

		user_obj = self.model(
			email = self.normalize_email(email)
		)

		user_obj.set_password(password)
		# user_obj.staff = estate
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staff_user(self, email, estate, password=None):
		user = self.create_user(
			email,
			password=password,
			estate = estate,
			is_staff=True
		)
		return user

	def create_superuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
			is_admin=True
		)
		return user

class User(AbstractBaseUser):
	email 		= models.EmailField(max_length=255, unique=True)
	# name 		= models.CharField(max_lengt=255, blank=True, null=True)
	# surname 	= models.CharField(max_lengt=255, blank=True, null=True)
	active 		= models.BooleanField(default=False)
	staff 		= models.BooleanField(default=False)
	admin 		= models.BooleanField(default=False)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login	= models.DateTimeField(verbose_name='last login', auto_now_add=True)
	estate  	= models.ForeignKey(EstateAgent, on_delete=models.CASCADE, blank=True, null=True)

	testfield  	= models.CharField(max_length=50)

	USERNAME_FIELD = 'email' #username
	REQUIRED_FIELDS = []

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_lable):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active
