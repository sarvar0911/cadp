from rest_framework import serializers
from .models import CustomUser, Region
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'email': self.user.email})
        return data
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)
    region = RegionSerializer(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(
        queryset=Region.objects.all(), source='region', write_only=True
    )
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'region', 'region_id', 'email', 'first_name', 'last_name',
                  'password', 'old_password']

    def validate(self, data):
        request_method = self.context['request'].method
        password = data.get('password')
        
        if request_method == 'POST':
            if not password:
                raise serializers.ValidationError({"info": "Please provide a password."})
        elif request_method in ['PUT', 'PATCH']:
            old_password = data.get('old_password')
            if password and not old_password:
                raise serializers.ValidationError({"info": "Please provide the old password."})
        
        return data 
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = instance
        password = validated_data.pop('password', None)
        old_password = validated_data.pop('old_password', None)
        
        if password and old_password:
            if not user.check_password(old_password):
                raise serializers.ValidationError({"info": "Old password is incorrect."})
            user.set_password(password)
        
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        user.save()
        
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        return value
