from django.urls import path
from .views import (
    NewsListAPIView, NewsDetailAPIView, 
    ProjectListAPIView, ProjectDetailAPIView, 
    AchievementListAPIView, AchievementDetailAPIView, 
    RecentlyUploadedNewsAPIView
)

urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('achievements/', AchievementListAPIView.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', AchievementDetailAPIView.as_view(), name='achievement-detail'),
    path('news/recent/', RecentlyUploadedNewsAPIView.as_view(), name='recent-news'),
]
