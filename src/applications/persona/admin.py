from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'firts_name',
        'last_name',
        'departamento', 
        'job',
        'full_name',
        'id',
        
    )

    # decorador que comcatena nombre y apellido
    def full_name(self, obj):        
        return obj.firts_name + ' ' + obj.last_name
     
    # agrega un buscador al admin
    search_fields = ('firts_name',)

    # agrega un filtrador
    list_filter = ('departamento', 'job', 'habilidades', )

    # filter habilidades
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
