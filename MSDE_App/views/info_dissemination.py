from django.shortcuts import render, redirect, get_object_or_404

# pragma: no cover
def info_dissemination(request):
    return render(request, '../templates/info_dissemination/information_dissemination.html')