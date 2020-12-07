from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Departamento(models.Model):
    """ 
    unique sirve para que no se repita el nombre
    
    """

    name = models.CharField('Nombre', max_length = 50, blank = True)
    shor_name = models.CharField('Nombre Corto', max_length = 20, unique = True)
    anulate = models.BooleanField('Anulado', default = False)    

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name') #evita que se agregue  dos cosas con el mismo nombre

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shor_name
