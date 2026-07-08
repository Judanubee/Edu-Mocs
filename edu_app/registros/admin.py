from django.contrib import admin
from .models import AdministradoresCursos, Alumnos, Profesores

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Profesores, AdministrarModelo)
admin.site.register(AdministradoresCursos, AdministrarModelo)