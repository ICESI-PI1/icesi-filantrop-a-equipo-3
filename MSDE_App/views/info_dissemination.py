from django.shortcuts import render, redirect, get_object_or_404


def info_dissemination(request): # pragma: no cover
    return render(request, '../templates/info_dissemination/information_dissemination.html')