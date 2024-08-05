from rest_framework import generics
from django.utils import translation
from .models import About, Goal, CentralOffice, TerritorialDivision
from .serializers import AboutSerializer, GoalSerializer, CentralOfficeSerializer, TerritorialDivisionSerializer
from django.utils.translation import get_language


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
    

class AboutListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class GoalListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class CentralOfficeListAPIView(generics.ListAPIView):
    queryset = CentralOffice.objects.all()
    serializer_class = CentralOfficeSerializer


class TerritorialDivisionListAPIView(generics.ListAPIView):
    queryset = TerritorialDivision.objects.all()
    serializer_class = TerritorialDivisionSerializer
