from django.contrib.auth.models import AbstractUser
from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.username
