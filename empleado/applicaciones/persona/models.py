from django.db import models
from applicaciones.departamento.models import Departamento
from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField
class Habilidades(models.Model):
	habilidad = models.CharField('Habilidad', max_length=50)

	class Meta:
		verbose_name='Habilidad'
		
	def __str__(self):
		return self.habilidad

# Create your models here.
class empleado(models.Model):
	tipo_job=(
          ('0','contador'),
          ('1','administrador'),
          ('2','economista'),
		)
	first_name = models.CharField('nombres', max_length=50)

	last_name =models.CharField('apellidos', max_length=50)

	full_name =models.CharField('nombres completos', max_length=120,blank=True)

	job=models.CharField('trabajo', max_length=1, choices=tipo_job)


	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

	habilidades = models.ManyToManyField(Habilidades)
	avatar=models.ImageField(upload_to='empleado',blank=True,null=True)
	hoja_vida = RichTextField()
	class Meta:
		verbose_name='Mi empleado'
		verbose_name_plural='Empleados de la empresa'
		ordering=['-first_name','last_name']
		unique_together=('first_name','departamento')
	def __str__(self):
		return str(self.id)+'-'+self.first_name+'--'+self.last_name
    