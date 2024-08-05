from django.db import models


class ContentBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reports_images/')
    file = models.FileField(upload_to='reports_files/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Report(ContentBase):
    MONTHLY = 'monthly'
    ANNUAL = 'annual'

    REPORT_CHOICES = [
        (MONTHLY, 'Monthly'),
        (ANNUAL, 'Annual'),
    ]

    report_type = models.CharField(max_length=10, choices=REPORT_CHOICES)

    def __str__(self):
        return self.title


class Grant(ContentBase):
    LOCAL = 'local'
    INTERNATIONAL = 'international'

    GRANT_CHOICES = [
        (LOCAL, 'Local'),
        (INTERNATIONAL, 'International'),
    ]

    grant_type = models.CharField(max_length=15, choices=GRANT_CHOICES)

    def __str__(self):
        return self.title
