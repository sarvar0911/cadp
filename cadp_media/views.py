from rest_framework import generics
from .models import Partner, PhotoGallery, VideoGallery
from .serializers import PartnerSerializer, PhotoGallerySerializer, VideoGallerySerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PhotoGalleryListView(generics.ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer


class VideoGalleryListView(generics.ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
