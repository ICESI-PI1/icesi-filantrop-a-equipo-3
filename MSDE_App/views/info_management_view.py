from django.shortcuts import render, redirect, get_object_or_404


def info_management(request):
    return render(request, '../templates/information_management/information_management.html')
