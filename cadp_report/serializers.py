from rest_framework import serializers
from .models import Report, Grant
    

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'report_type', 'description', 'image', 'file']
    
    
class GrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grant
        fields = ['id', 'title', 'grant_type', 'description', 'image', 'file']
