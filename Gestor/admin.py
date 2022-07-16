from django.contrib import admin
from .models import Estante, Oficina, Empresa, Empleado
from django.utils.html import format_html
from django.utils.safestring import mark_safe

@admin.register(Empresa)
class GestionEmpresa(admin.ModelAdmin):
   list_display = ('nempresa', 'imgref',)
   list_display_links = ('nempresa',)


@admin.register(Empleado)
class GestionEmpleado(admin.ModelAdmin):
    list_display = ('cedula', 'primerApellido', 'primerNombre',)
    list_filter = ('status', 'genero',)
    search_fields = ('cedula', 'primerApellido', 'primerNombre',)
    list_display_links = ('cedula',)
    list_per_page = 5


@admin.register(Estante)
class GestionEstante(admin.ModelAdmin):
    list_display = ('ubicacion',)
    list_display_links = ('ubicacion',)


@admin.register(Oficina)
class GestionOficina(admin.ModelAdmin):
    list_display = ('noficina',)
    list_display_links = ('noficina',)
