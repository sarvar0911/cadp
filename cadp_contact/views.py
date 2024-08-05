from rest_framework import generics
from .models import Contact, Message
from .serializers import ContactSerializer, MessageSerializer

class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_object(self):
        return Contact.get_solo()


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
