from rest_framework import generics
from django.utils import translation
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import News, Project, Achievement
from .serializers import NewsSerializer, ProjectSerializer, AchievementSerializer
from django.utils.translation import get_language


class IncrementViewCountRetrieveAPIView(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LanguageMixin:
    
    def get_queryset(self):
        # lang = self.get_language_from_request(self.request)
        lang = get_language()
        # print("The lang : ", lang)
        translation.activate(lang)
        
        filter_args = {}
        title_field = f'title_{lang}'
        description_field = f'description_{lang}'
        
        if hasattr(self.queryset.model, title_field):
            filter_args[f'{title_field}__isnull'] = False
        
        if hasattr(self.queryset.model, description_field):
            filter_args[f'{description_field}__isnull'] = False
        
        return super().get_queryset().filter(**filter_args)


class NewsListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailAPIView(LanguageMixin, IncrementViewCountRetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ProjectListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(LanguageMixin, IncrementViewCountRetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AchievementListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementDetailAPIView(LanguageMixin, IncrementViewCountRetrieveAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class RecentlyUploadedNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):

        recent_date = timezone.now() - timezone.timedelta(days=7)
        queryset = News.objects.filter(date__gte=recent_date).order_by('-date')
        
        return queryset
    