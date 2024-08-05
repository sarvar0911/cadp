from django.urls import path
from .views import PartnerListView, PhotoGalleryListView, VideoGalleryListView


urlpatterns = [
    path('partners/', PartnerListView.as_view(), name='partner-list'),
    path('photogallery/', PhotoGalleryListView.as_view(), name='photogallery-list'),
    path('videogallery/', VideoGalleryListView.as_view(), name='videogallery-list'),
]
