from django.contrib import admin
from .models import News, Project, Achievement


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'description')
    list_filter = ('category', 'date')
    exclude = ('views_count', 'date', 'title', 'description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    exclude = ('views_count', 'date', 'title', 'description')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    exclude = ('views_count', 'date', 'title', 'description')
