from django.db import models
from django.utils import timezone

class Marca(models.Model):
	marca = models.CharField(max_length=50)
	origen = models.CharField(max_length=50)

	def __str__(self):
		return self.marca


class Modelo(models.Model):
	modelo = models.CharField(max_length=50)
	marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
	def __str__(self):
		return '{} {}'.format(self.marca.marca, self.modelo)


class tipoAuto(models.Model):
	nombre_tipo = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre_tipo


class Auto(models.Model):
	modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)	
	tipoAuto = models.ForeignKey('tipoAuto',on_delete=models.CASCADE)

	def __str__(self):
		return '{} {} {}'.format(self.modelo.marca.marca, self.modelo.modelo, self.tipoAuto.nombre_tipo)

class Publicacion(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	foto = models.CharField(max_length=100)
	fecha = models.DateTimeField(blank=True, null=True)
	kilometraje = models.IntegerField()
	precio = models.IntegerField()
	auto = models.ForeignKey('Auto', on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.titulo,self.descripcion)

