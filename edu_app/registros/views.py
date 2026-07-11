from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class LoginPersonalizado(LoginView):
    template_name = "inicio/login.html"

    def get_success_url(self):
        return reverse_lazy("principal")