from django.shortcuts import render, redirect, get_object_or_404

def info_dissemination(request):
    return render(request, '../templates/information_dissemination/information_dissemination.html')