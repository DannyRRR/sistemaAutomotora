from django.contrib import admin
from .models import Marca, Modelo, tipoAuto, Auto, Publicacion

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(tipoAuto)
admin.site.register(Auto)
admin.site.register(Publicacion)