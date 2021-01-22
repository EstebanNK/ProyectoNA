from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 5
    model = Empleado
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
             first_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 10
    model = Empleado
    context_object_name = 'lista'


class ListByAreaEmpleado(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        area = self.kwargs['shor_name']

        lista = Empleado.objects.filter(
            departamento__shor_name= area
        )

        return lista



class ListByKeyWord(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        return lista



class ListHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)

        return empleado.habilidades.all()
    


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"




class SuccessView(TemplateView):
    template_name = "empleados/success.html"




class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):

        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)




class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')





class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')
