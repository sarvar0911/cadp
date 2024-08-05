from django.db import models
from tinymce.models import HTMLField

class ContentBase(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)
    views_count = models.IntegerField(default=0, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    description = HTMLField()

    class Meta:
        abstract = True

class News(ContentBase):
    CENTER_NEWS = 'center'
    UZBEKISTAN_NEWS = 'uzbekistan'
    INTERNATIONAL_NEWS = 'international'
    
    NEWS_CHOICES = [
        (CENTER_NEWS, 'Center News'),
        (UZBEKISTAN_NEWS, 'Uzbekistan News'),
        (INTERNATIONAL_NEWS, 'International News'),
    ]

    category = models.CharField(max_length=20, choices=NEWS_CHOICES, default=CENTER_NEWS)
    links = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title


class Project(ContentBase):
    def __str__(self):
        return self.title


class Achievement(ContentBase):
    def __str__(self):
        return self.title
