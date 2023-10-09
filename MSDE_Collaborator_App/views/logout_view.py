from django.contrib.auth import logout
from django.shortcuts import redirect


def salir(request):
    logout(request)
    return redirect('/')
