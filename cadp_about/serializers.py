from rest_framework import serializers
from .models import About, Goal, CentralOffice, TerritorialDivision


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'description', 'image']


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['title', 'description']


class CentralOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralOffice
        fields = ['first_name', 'last_name', 'position', 'phone', 'email', 'work_days', 'address']


class TerritorialDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerritorialDivision
        fields = ['city', 'address', 'phone']
