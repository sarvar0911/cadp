from django.contrib import admin
from .models import Contact, Message
from solo.admin import SingletonModelAdmin

@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    list_display = ['phone', 'address', 'email']
    fields = ['phone', 'address', 'work_days', 'email', 'telegram_link',
              'facebook_link', 'youtube_link', 'latitude', 'longitude']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'checked', 'message']
    list_filter = ['checked']
    search_fields = ['name', 'phone', 'message']
    fields = ['name', 'phone', 'message', 'checked']
