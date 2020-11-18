from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer, UserDetailsSerializer

from .models import Hotel


UserModel = get_user_model()


class HotelSerializer(serializers.ModelSerializer):
    """Serializer for Hotel model"""

    class Meta:
        model = Hotel
        fields = '__all__'


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""

    username = None

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    username = None


class CustomUserDetailsSerializer(UserDetailsSerializer):
    """
    Custom User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'email', 'name')
        read_only_fields = ('email', )
