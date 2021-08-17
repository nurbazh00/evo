from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from .serializers import *
from apps.audios.models import Audio, Category


class AudioList(ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class AudioDetail(RetrieveUpdateDestroyAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioDetailSerializer


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

