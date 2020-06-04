from django import forms 

from .models import Prueba
class PruebaForm(forms.ModelForm):
	class Meta:
		model=Prueba
		fields=(
			'titulo',
			'subtitulo'
			)
		widgets={
		   'subtitulo':forms.TextInput(
		   		attrs={
		   		   'placeholder':'Ingrese el texto aqui',
		   		}
		   	)
		}
	def clean_titulo(self):
		titulo=self.cleaned_data['titulo']
		if titulo == 'hola':
			raise forms.ValidationError('Ingrese otro titulo diferente titulo')
		return titulo	
