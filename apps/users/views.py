from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import (AuthSerializer,
    CustomUserDetailSerializer, CustomUsersCreateSerializer,)

from apps.users.models import CustomUser


class UserAuthView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = CustomUser.objects.filter\
            (email=serializer.data.get('email')).first()

        if user is None:
            return Response(
                data={'error': 'Пользотеватель не найден'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not user.check_password(serializer.data.get('password')):
            return Response(
                data={'error': 'Не верный пароль'},
                status=status.HTTP_404_NOT_FOUND,
            )

        user_token, created = Token.objects.get_or_create(user=user)

        return Response(data={'token': user_token.key},
                        status=status.HTTP_200_OK)


class UsersListCreateAPIView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUsersCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.password = make_password(instance.password)
        instance.save()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserDetailSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
