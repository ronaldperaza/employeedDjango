
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

#dos lineas para generar urls de los archivos staticos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.departamento.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.persona.urls')) 

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
