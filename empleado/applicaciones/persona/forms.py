from django import forms

from .models import empleado

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = empleado
		fields=(
			'first_name',
			'last_name',
			'job',
			'departamento',
			'avatar',
			'habilidades',
		)
		widgets={
		 	'habilidades': forms.CheckboxSelectMultiple()
		}