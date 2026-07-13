<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from registros.models import Cursos, Alumnos
=======
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
>>>>>>> origin/zaid

# Importación de modelos desde tu app registros
from registros.models import Cursos, Profesores

<<<<<<< HEAD
=======
# Create your views here.

>>>>>>> origin/zaid
@login_required
def principal(request):
    cursos = Cursos.objects.all()

<<<<<<< HEAD
=======
    es_alumno = False
    es_profesor = False
    if request.user.is_authenticated:
        es_alumno = hasattr(request.user, "perfil_alumno")
        es_profesor = hasattr(request.user, "perfil_profesor")

>>>>>>> origin/zaid
    return render(request, "inicio/principal.html", {
        "cursos": cursos,
    })

<<<<<<< HEAD

@login_required
def cursos(request):
    cursos_disponibles = Cursos.objects.all()
=======
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
>>>>>>> origin/zaid

    return render(request, "inicio/cursos.html", {
        "cursos": cursos_disponibles,
    })


@login_required
def contacto(request):
<<<<<<< HEAD
    return render(request, "inicio/contacto.html")
=======
    profesores = Profesores.objects.all() 
    return render(request, "inicio/contacto.html", {
        "profesores": profesores
    }) 
>>>>>>> origin/zaid


@login_required
def perfil(request):
    return render(request, "inicio/perfil.html")


@login_required
def perfil_alumno(request):
<<<<<<< HEAD
    alumno = get_object_or_404(
        Alumnos,
        usuario=request.user
    )

    return render(request, "inicio/perfil_alumno.html", {
        "alumno": alumno,
        "cursos": alumno.cursos.all(),
    })

=======
    return render(request, "inicio/perfil_alumno.html")
>>>>>>> origin/zaid

@login_required
def perfil_profesor(request):
    return render(request, "inicio/perfil_profesor.html")


@login_required
def curso_info(request, id):
    curso = get_object_or_404(Cursos, id=id)

    return render(request, "inicio/curso_info.html", {
        "curso": curso,
    })


@login_required
@require_POST
def inscribirse_curso(request, id):
    curso = get_object_or_404(Cursos, id=id)

    try:
        alumno = request.user.perfil_alumno
    except Alumnos.DoesNotExist:
        messages.error(
            request,
            "Tu usuario no tiene un perfil de alumno."
        )
        return redirect("curso_info", id=id)

    alumno.cursos.add(curso)

    messages.success(
        request,
        f"Te inscribiste correctamente al curso {curso.nombre}."
    )

    return redirect("curso_info", id=id)