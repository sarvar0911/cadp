from django.urls import path
from .views import AboutListAPIView, GoalListAPIView, CentralOfficeListAPIView, TerritorialDivisionListAPIView


urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about-list'),
    path('goals/', GoalListAPIView.as_view(), name='goal-list'),
    path('central-offices/', CentralOfficeListAPIView.as_view(), name='central-office-list'),
    path('territorial-divisions/', TerritorialDivisionListAPIView.as_view(), name='territorial-division-list'),
]
