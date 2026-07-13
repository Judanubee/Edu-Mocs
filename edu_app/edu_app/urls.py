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
from edu_app import settings
from inicio import views 
from django.contrib.auth import views as auth_views
from registros.views import LoginPersonalizado




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
    path("curso_info/", views.curso_info, name="curso_info"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
