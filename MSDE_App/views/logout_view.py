from django.contrib.auth import logout
from django.shortcuts import redirect


def salir(request): # pragma: no cover
    logout(request)
    return redirect('/')

