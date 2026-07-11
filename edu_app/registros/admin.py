from django.contrib import admin
from django.utils.html import format_html

from .models import AdministradoresCursos, Alumnos, Profesores, Cursos

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Profesores, AdministrarModelo)
admin.site.register(AdministradoresCursos, AdministrarModelo)
admin.site.register(Cursos, AdministrarModelo)