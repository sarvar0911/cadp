from django.contrib import admin
from .models import CustomUser, Region
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Region)