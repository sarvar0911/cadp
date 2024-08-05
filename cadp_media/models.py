from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit


class Partner(models.Model):
    LOCAL = 'local'
    INTERNATIONAL = 'international'

    PARTNER_CHOICES = [
        (LOCAL, 'Local'),
        (INTERNATIONAL, 'International'),
    ]

    partner_type = models.CharField(max_length=15, choices=PARTNER_CHOICES)
    image = models.ImageField(upload_to='partners/')
    link = models.URLField()

    def __str__(self):
        return f"{self.get_partner_type_display()} Partner"


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='photos/')
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(100)],
        format='JPEG',
        options={'quality': 10}
    )

    def __str__(self):
        return f"Photo {self.id}"


class VideoGallery(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
