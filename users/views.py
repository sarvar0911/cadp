from django.conf import settings
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CustomUser
from .serializers import UserSerializer, ChangePasswordSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .tasks import send_email_task
from .models import CustomUser
from rest_framework import status
from rest_framework.views import APIView


class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            subject = data['subject']
            message = data['message']
            from_email = settings.EMAIL_HOST_USER
            region_id = data.get('region_id', None)

            if region_id:
                users = CustomUser.objects.filter(region_id=region_id)
            else:
                users = CustomUser.objects.all()

            recipient_list = [user.email for user in users if user.email]

            if recipient_list:
                send_email_task.delay(subject, message, from_email, recipient_list)
                return Response({'status': 'Emails sent successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'No recipients found!'}, status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            return Response({'error': f'Missing key: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(UserViewSet, self).get_permissions()
    
    def create(self, request, *args, **kwargs):
        response = super(UserViewSet, self).create(request, *args, **kwargs)
        return Response({"info": "User created successfully", "user": response.data})
    
    def update(self, request, *args, **kwargs):
        response = super(UserViewSet, self).update(request, *args, **kwargs)
        return Response({"info": "User updated successfully", "user": response.data})
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')
        
        if not user.check_password(old_password):
            return Response({"info": "Old password is incorrect"}, status=400)
        
        user.set_password(new_password)
        user.save()
        
        return Response({"info": "Password changed successfully"})

    def get_serializer_class(self):
        if self.action == 'change_password':
            return ChangePasswordSerializer
        return super(UserViewSet, self).get_serializer_class()
