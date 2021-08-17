from django.urls import path

from apps.users.views import (
    UsersListCreateAPIView,
    UserAuthView,
    UserRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('auth', UserAuthView.as_view(), name='auth'),
    path('users/', UsersListCreateAPIView.as_view(), name='users'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view())
]