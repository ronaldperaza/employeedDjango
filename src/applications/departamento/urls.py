from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app"

urlpatterns = [
    path("departamento-lista/", views.DepartamentoListView.as_view(), name="lista_departamento"),
    path("new-departamento/", views.NewDepartamentoView.as_view(), name="nuevo_departamento"),
]
