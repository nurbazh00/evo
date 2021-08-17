from django.urls import path

from apps.audios.views import (
    AudioList, AudioDetail,
    CategoryList, CategoryDetail
)

urlpatterns = [
    path('audios/', AudioList.as_view(), name='audios'),
    path('audios/<int:pk>', AudioDetail.as_view()),

    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetail.as_view())
]