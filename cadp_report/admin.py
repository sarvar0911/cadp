from django.contrib import admin
from .models import Report, Grant


class ReportAdmin(admin.ModelAdmin):
    exclude = ('date',)
    list_display = ('title', 'report_type')
    search_fields = ('title', 'report_type')
    list_filter = ('report_type',)
    exclude = ('title', 'description')


class GrantAdmin(admin.ModelAdmin):
    exclude = ('date',)
    list_display = ('title', 'grant_type')
    search_fields = ('title', 'grant_type')
    list_filter = ('grant_type',)
    exclude = ('title', 'description')


admin.site.register(Report, ReportAdmin)
admin.site.register(Grant, GrantAdmin)
