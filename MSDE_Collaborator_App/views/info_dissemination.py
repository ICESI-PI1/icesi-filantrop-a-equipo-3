from django.shortcuts import render, redirect, get_object_or_404


def info_dissemination(request):
    return render(request, '../templates/info_dissemination_collaborator/information_dissemination.html')