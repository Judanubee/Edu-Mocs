from django.db import models

# Create your models here.
class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12) #Texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla

class Profesores(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12) #Texto corto
    nombre = models.TextField() #Texto largo
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla

class AdministradoresCursos(models.Model): #Define la estructura de nuestra tabla
    nombre = models.TextField() #Texto largo
    correo = models.EmailField() #Texto largo
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Administrador de Cursos"
        verbose_name_plural = "Administradores de Cursos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo
    def __str__(self):
        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla

