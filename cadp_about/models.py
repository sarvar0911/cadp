from django.db import models
from tinymce.models import HTMLField
from solo.models import SingletonModel  


class About(SingletonModel):
    title = models.CharField(max_length=255)
    description = HTMLField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'
    
    def __str__(self):
        return self.title
    


class Goal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class CentralOffice(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    work_days = models.CharField(max_length=100)
    address = models.TextField()
    
    class Meta:
        verbose_name_plural = 'central office'
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'
    

class TerritorialDivision(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.city} - {self.phone}'
