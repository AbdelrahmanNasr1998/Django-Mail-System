from django.contrib import admin

# Register your models here.

from .models import Accounts
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = Accounts
    search_fields = ('email', 'username',)
    list_filter = ('is_active', 'is_staff',)
    list_display = ('email', 'username',)
    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password')}),



    )

admin.site.register(Accounts, UserAdminConfig)


