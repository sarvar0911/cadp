from django.urls import path
from .views import ReportListAPIView, GrantListAPIView


urlpatterns = [
    path('reports/', ReportListAPIView.as_view(), name='report-list'),
    path('grants/', GrantListAPIView.as_view(), name='grant-list'),
]
