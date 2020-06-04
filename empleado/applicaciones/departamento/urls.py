from django.contrib import admin
from django.urls import path
from .  import views

app_name="departamento_app"

urlpatterns = [
	path('new_departamento/',views.newDepartamentoView.as_view(),name='nuevo_departamentos'),
	path('departamento_list/',views.DepartamentoListView.as_view(),name='departamento_list'),
]

