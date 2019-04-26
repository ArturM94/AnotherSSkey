from django.contrib import admin

from keystorage.models import User


class UserAdmin(admin.ModelAdmin):
    """User model for admin panel"""
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login')


admin.site.register(User, UserAdmin)
