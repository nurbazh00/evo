from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


v1 = ([
    path('', include('apps.audios.urls')),
    path('', include('apps.users.urls')),
], 'v1')

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
]


urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
