from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (   
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Empleado

class InicioView(TemplateView):
    """ Vista que carga la pagiande inicio """
    template_name = "inicio.html"

class ListAllEmpleado(ListView):    
    """ lista de todos los empleado """
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'firts_name'
    context_object_name = 'empleados'
    

    """ funncion para realizar filtraciones en el buscar
        icontains bucar cualquier letra en las palabras
    """
    def get_queryset(self):
        
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            firts_name__icontains= palabra_clave         
        )
        return lista


class ListByAreaEmpleado(ListView):    
    """ lista empleado que pertenecen a un area """

    template_name = "persona/list_by_area.html"
    context_object_name = "empleados"
    
    def get_queryset(self):
        # kwargs sirve para recoger lo que nos envian por url
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area 
        )
        return lista


class ListaEmpleadoAdmin(ListView):    
    """ lista de todos los empleado """
    template_name = "persona/lista_empleados.html"
    paginate_by = 6
    ordering = 'firts_name'
    context_object_name = 'empleados'
    model = Empleado    



class listEmpleadoByKwords(ListView):
    """ lista de empleado por palabra Clave """
    template_name = 'persona/by_kwords.html'
    context_object_name = 'empleados'

    """ funncion para realizar filtraciones """
    def get_queryset(self):
        print("******************")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            firts_name = palabra_clave 
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        """ recupera unico registro de la base de datos """
        empleado = Empleado.objects.get(id = 7)
        # print(empleado.habilidades.all())        
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs) 
        context['titulo'] = 'Employeed of the month'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"




class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # estos son los campos que queremos mostrar
    fields = [
        'firts_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.firts_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"

    # estos son los campos que queremos actualizar
    fields = [
        'firts_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        return super().post(request, *args, **kwargs)
    

    def form_valid(self, form):
        return super(EmpleadoUpdateView,self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"

    success_url = reverse_lazy('persona_app:empleados_admin')
