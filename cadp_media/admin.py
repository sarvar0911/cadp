from django.contrib import admin
from .models import Partner, PhotoGallery, VideoGallery


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'partner_type', 'link']
    list_filter = ['partner_type']
    search_fields = ['partner_type']


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_filter = ['image']
    exclude =['thumbnail']

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'video_file']
    search_fields = ['title']

