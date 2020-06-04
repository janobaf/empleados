from django.contrib import admin
from django.urls import path
from .  import views

app_name="persona_app"

urlpatterns = [

	path('listar_empleado',views.ListEmpleadosAdmin.as_view(),name='listar_empleado_admin'),
	path('',views.inicioView.as_view(),name="inicio"),
    path('listar-todo-empleado/',views.ListAllempleados.as_view(),name="empleados_all"),
	path('listar-area/<shorname>',views.ListByAreaempleado.as_view(),name="empleados_lista"),
	path('buscar_empleado/',views.ListEmpleadosByKword.as_view()),
	path('listar_habilidades/',views.Lista_Habilidades.as_view()),
	path('ver_empleado/<pk>',views.EmpleadoDetailView.as_view(),name="empleado_detail"),
	path('add_empleado/',views.EmpleadoCreateView.as_view(),name="añadir_empleado"),
	path('succes/',views.SuccessView.as_view(),name='correcto'),
	path('update_empleado/<pk>',views.EmpleadoUpdateView.as_view(),name="modificar"),		
	path('delete_empleado/<pk>',views.EmpleadoDeleteView.as_view(),name="delete"),			
]

