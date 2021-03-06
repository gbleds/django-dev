from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_joined','last_login', 'estate', 'admin',)
    list_filter = ('admin', 'estate',)
    readonly_fields = ('date_joined','last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_joined', 'last_login')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active', 'estate')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'estate')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
