from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import CustomUser


class AuthSerializer(Serializer):
    email = serializers.EmailField(max_length=60)
    password = serializers.CharField(max_length=128)


class CustomUsersCreateSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'first_name', 'last_name', 'email', 'dob', 'gender',
            'country', 'city', 'password',
        )


class CustomUserDetailSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'first_name', 'last_name', 'email', 'dob', 'gender',
            'country', 'city', 'avatar',
        )