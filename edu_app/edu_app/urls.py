"""
URL configuration for edu_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from inicio import views 
from registros.views import LoginPersonalizado
from registros import views as registros_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('cursos/', views.cursos, name='cursos'),
    path('contacto/', views.contacto, name='contacto'),
    path('perfil/', views.perfil, name='perfil'),
    path("login/",LoginPersonalizado.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("perfil_alumno/", views.perfil_alumno, name="perfil_alumno"),
    path("perfil_profesor/", views.perfil_profesor, name="perfil_profesor"),
    path(
        "curso_info/<int:id>/",
        views.curso_info,
        name="curso_info"
    ),
      path(
        "inscribirse_curso/<int:id>/",
        views.inscribirse_curso,
        name="inscribirse_curso"
    ),
    path(
    "panel-administrador/",
    registros_views.panel_administrador,
    name="panel_administrador"
),

path(
    "panel-administrador/alumnos/nuevo/",
    registros_views.registrar_alumno,
    name="registrar_alumno"
),

path(
    "panel-administrador/profesores/nuevo/",
    registros_views.registrar_profesor,
    name="registrar_profesor"
),

path(
    "panel-administrador/cursos/nuevo/",
    registros_views.registrar_curso,
    name="registrar_curso"
),
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
