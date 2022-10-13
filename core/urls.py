from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from rest_framework import routers
from todos.views import ToDoViewset

router = routers.SimpleRouter()
router.register(r'api/tasks', ToDoViewset, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
] + router.urls


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)