
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.departamento.urls')),
    path('', include('applications.home.urls')),
    path('', include('applications.persona.urls')) 

]
