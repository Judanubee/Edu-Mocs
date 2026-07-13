from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Alumnos, Profesores, Cursos

class AlumnoUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=150)
    perfil = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "nombre",
            "perfil",
        )

class ProfesorUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=150)

    desc_profesor = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    perfil = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "nombre",
            "desc_profesor",
            "perfil",
        )
class CursoForm(forms.ModelForm):

    class Meta:
        model = Cursos

        fields = (
            "nombre",
            "descripcion",
            "categoria",
            "horas",
            "profesor",
            "imagen",
        )

        widgets = {
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 5
                }
            )
        }