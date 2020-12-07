from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad

class Empleado(models.Model):
    """ modelo para tabla empleado """
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )


    firts_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=123, blank=True)
    job = models.CharField('Trabajos', max_length=60, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank = True, null = 'True')
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida =  RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-firts_name', 'last_name']
        unique_together = ('firts_name', 'departamento') #evita que se agregue  dos cosas con el mismo nombre


    def __str__(self):
        return str(self.id) + ' - ' + self.firts_name + ' - ' + self.last_name