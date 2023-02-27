from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static #this is needed for file and image upload
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('appManager.urls', namespace = 'appManager')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
