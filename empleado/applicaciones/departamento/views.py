from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit  import FormView
# Create your views here.
from .forms import DepartamentoForm
from applicaciones.persona.models import empleado
from .models import Departamento

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'

class newDepartamentoView(FormView):
	template_name ='departamento/new_departamento.html'
	form_class=DepartamentoForm
	success_url='/'
	def form_valid(self,form):
		print('ingreso')
		depa=Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shor_name']
		)
		depa.save()

		nombre=form.cleaned_data['nombre']
		apellidos=form.cleaned_data['apellidos']
		empleado.objects.create(
			first_name=nombre,
			last_name =apellidos,
			job='1',
			departamento=depa
		)
			
		return super(newDepartamentoView,self).form_valid(form)