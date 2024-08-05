from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import About, Goal, CentralOffice, TerritorialDivision


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    list_display = ('title',)
    exclude = ('title', 'description')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    exclude = ('title', 'description')



@admin.register(CentralOffice)
class CentralOfficeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'position', 'email')
    list_filter = ('position', 'work_days')


@admin.register(TerritorialDivision)
class TerritorialDivisionAdmin(admin.ModelAdmin):
    list_display = ('city', 'phone')
    search_fields = ('city', 'address', 'phone')
