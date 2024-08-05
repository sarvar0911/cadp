from rest_framework import serializers
from .models import Partner, PhotoGallery, VideoGallery

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class PhotoGallerySerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)  # Ensure thumbnail is read-only

    class Meta:
        model = PhotoGallery
        fields = '__all__'  # Include all fields

class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = '__all__'
