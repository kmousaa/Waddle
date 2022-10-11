""" Configuration of administritive interface for microblogs """
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Confirguration of the admin interface for users"""
    list_display =  [
        'username', 'first_name', 'last_name' , 'email' , 'is_active',
    ]

    #allows us to specify attribuites that are includded in table of view of users
