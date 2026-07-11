from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from registros.models import Cursos


# Create your views here.
@login_required
def principal(request):

    cursos = Cursos.objects.all()

    es_alumno = False
    es_profesor = False
    if request.user.is_authenticated:
        es_alumno = hasattr(request.user, "perfil_alumno")
        es_profesor = hasattr(request.user, "perfil_profesor")

    return render(request, "inicio/principal.html",{
        "cursos": cursos,
        "es_alumno": es_alumno,
        "es_profesor": es_profesor
    })

@login_required
def cursos(request):
    return render(request, "inicio/cursos.html")

def contacto(request):
    return render(request, "inicio/contacto.html") 

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