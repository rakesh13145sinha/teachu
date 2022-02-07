from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
# class RegistrationAdmin(admin.ModelAdmin):
#     list_displays=['name','phone','course']

admin.site.register(Registration)