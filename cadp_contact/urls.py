from django.urls import path
from .views import ContactDetailView, MessageCreateView


urlpatterns = [
    path('contact/', ContactDetailView.as_view(), name='contact-detail'),
    path('message/', MessageCreateView.as_view(), name='message-create'),
]
