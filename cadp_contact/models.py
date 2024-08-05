from django.db import models
from solo.models import SingletonModel


class Contact(SingletonModel):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    work_days = models.CharField(max_length=100)
    email = models.EmailField()
    telegram_link = models.URLField(blank=True, null=True)  
    facebook_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.address


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"
