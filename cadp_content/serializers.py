from rest_framework import serializers
from .models import News, Project, Achievement
    
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'category', 'links', 'description', 'views_count', 'date']
        read_only_fields = ['views_count', 'date']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'views_count', 'date']
        read_only_fields = ['views_count', 'date']


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'title', 'description', 'views_count', 'date']
        read_only_fields = ['views_count', 'date']
