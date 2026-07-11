from django.db import models
from django.conf import settings
# Create your models here.

class Profesores(models.Model):
    nombre = models.CharField(max_length=150)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_profesor")    
    desc_profesor = models.TextField(null=True, blank=True)
    perfil = models.ImageField(upload_to="profesores/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
class Cursos(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.CharField(max_length=100)
    horas = models.PositiveIntegerField()
    profesor = models.ForeignKey(Profesores, on_delete=models.SET_NULL, null=True, blank=True, related_name="cursos")
    imagen = models.ImageField(
        upload_to="cursos/",
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Alumnos(models.Model):
    nombre = models.CharField(max_length=150)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_alumno"
    )
    cursos = models.ManyToManyField(
        Cursos,
        blank=True,
        related_name="alumnos"
    )
    cursos_favoritos = models.ManyToManyField(
        Cursos,
        blank=True,
        related_name="alumnos_favoritos"
    )
    perfil = models.ImageField(
        upload_to="alumnos/",
        null=True,
        blank=True
    )   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class AdministradoresCursos(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=128)
    nombre = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Administrador de cursos"
        verbose_name_plural = "Administradores de cursos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
