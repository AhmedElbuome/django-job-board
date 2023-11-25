from django.contrib import admin
from .models import Profile

# Register your models here.


# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Profile)