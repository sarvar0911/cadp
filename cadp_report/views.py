from rest_framework import generics
from .models import Report, Grant
from .serializers import ReportSerializer, GrantSerializer
from django.utils import translation
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
    
    
class ReportListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class GrantListAPIView(LanguageMixin, generics.ListAPIView):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer
    