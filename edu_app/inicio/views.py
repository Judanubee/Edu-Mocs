from django.shortcuts import render, HttpResponse

# Create your views here.
def principal(request):
    return render(request, "inicio/principal.html")

def cursos(request):
    return render(request, "inicio/cursos.html")

def contacto(request):
    return render(request, "inicio/contacto.html") 

def login(request):
    return render(request, "inicio/login.html")

def perfil(request):    
    return render(request, "inicio/perfil.html")
