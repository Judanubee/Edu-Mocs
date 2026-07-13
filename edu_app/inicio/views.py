from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from registros.models import Cursos, Alumnos, Profesores


@login_required
def principal(request):
    cursos = Cursos.objects.all()

    return render(request, "inicio/principal.html", {
        "cursos": cursos,
    })

@login_required
def curso_detalle(request, id):
    curso = get_object_or_404(Cursos, id=id)

    return render(request, "inicio/curso_detalle.html", {
        "curso": curso,
    })


@login_required
def contacto(request):
    profesores = Profesores.objects.all()

    return render(request, "inicio/contacto.html", {
        "profesores": profesores,
    })


@login_required
def perfil(request):
    return render(request, "inicio/perfil.html")


@login_required
def perfil_alumno(request):
    alumno = get_object_or_404(
        Alumnos,
        usuario=request.user
    )

    return render(request, "inicio/perfil_alumno.html", {
        "alumno": alumno,
        "cursos": alumno.cursos.all(),
    })


@login_required
def perfil_profesor(request):
    profesor = get_object_or_404(
        Profesores,
        usuario=request.user
    )

    return render(request, "inicio/perfil_profesor.html", {
        "profesor": profesor,
        "cursos": profesor.cursos.all(),
    })


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