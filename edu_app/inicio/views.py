from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Importación de modelos desde tu app registros
from registros.models import Cursos, Profesores

# Create your views here.

@login_required
def principal(request):
    cursos = Cursos.objects.all()

    es_alumno = False
    es_profesor = False
    if request.user.is_authenticated:
        es_alumno = hasattr(request.user, "perfil_alumno")
        es_profesor = hasattr(request.user, "perfil_profesor")

    return render(request, "inicio/principal.html", {
        "cursos": cursos,
        "es_alumno": es_alumno,
        "es_profesor": es_profesor
    })

# VISTA 1: El catálogo completo (Para ver TODOS los cursos)
@login_required
def cursos(request):
    lista_cursos = Cursos.objects.all() # Trae todos los cursos de la BD
    return render(request, "inicio/cursos.html", {
        "cursos": lista_cursos  # Pasa la lista completa al HTML
    })

# VISTA 2: El detalle de UN curso (Para la página con banner, horas e instructor)
@login_required
def curso_detalle(request, id):
    curso = get_object_or_404(Cursos, id=id)
    return render(request, "inicio/curso_detalle.html", {
        "curso": curso
    })

def contacto(request):
    profesores = Profesores.objects.all() 
    return render(request, "inicio/contacto.html", {
        "profesores": profesores
    }) 

def login(request):
    return render(request, "inicio/login.html")

def perfil(request):    
    return render(request, "inicio/perfil.html")
    
@login_required
def perfil_alumno(request):
    return render(request, "inicio/perfil_alumno.html")

@login_required
def perfil_profesor(request):
    return render(request, "inicio/perfil_profesor.html")