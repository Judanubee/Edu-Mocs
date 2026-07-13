from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import (
    AlumnoUsuarioForm,
    ProfesorUsuarioForm,
    CursoForm,
)
from .models import Alumnos, Profesores, Cursos

# Create your views here.
class LoginPersonalizado(LoginView):
    template_name = "inicio/login.html"

    def get_success_url(self):
        return reverse_lazy("principal")
    
@staff_member_required(login_url="login")
def panel_administrador(request):

    alumnos = Alumnos.objects.all()
    profesores = Profesores.objects.all()
    cursos = Cursos.objects.all()

    return render(
        request,
        "registros/panel_administrador.html",
        {
            "alumnos": alumnos,
            "profesores": profesores,
            "cursos": cursos,
        }
    )

@staff_member_required(login_url="login")
def registrar_alumno(request):

    if request.method == "POST":
        form = AlumnoUsuarioForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.email = form.cleaned_data["email"]
            usuario.save()

            Alumnos.objects.create(
                usuario=usuario,
                nombre=form.cleaned_data["nombre"],
                perfil=form.cleaned_data.get("perfil"),
            )

            messages.success(
                request,
                "Alumno registrado correctamente."
            )

            return redirect("panel_administrador")

    else:
        form = AlumnoUsuarioForm()

    return render(
        request,
        "registros/registrar_alumno.html",
        {
            "form": form
        }
    )
@staff_member_required(login_url="login")
def registrar_profesor(request):

    if request.method == "POST":
        form = ProfesorUsuarioForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.email = form.cleaned_data["email"]
            usuario.save()

            Profesores.objects.create(
                usuario=usuario,
                nombre=form.cleaned_data["nombre"],
                desc_profesor=form.cleaned_data[
                    "desc_profesor"
                ],
                perfil=form.cleaned_data.get("perfil"),
            )

            messages.success(
                request,
                "Profesor registrado correctamente."
            )

            return redirect("panel_administrador")

    else:
        form = ProfesorUsuarioForm()

    return render(
        request,
        "registros/registrar_profesor.html",
        {
            "form": form
        }
    )
@staff_member_required(login_url="login")
def registrar_curso(request):

    if request.method == "POST":
        form = CursoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Curso registrado correctamente."
            )

            return redirect("panel_administrador")

    else:
        form = CursoForm()

    return render(
        request,
        "registros/registrar_curso.html",
        {
            "form": form
        }
    )