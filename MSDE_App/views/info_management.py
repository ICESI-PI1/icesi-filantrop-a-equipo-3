from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.views import home_view


def info_management(request):
    return render(request, '../templates/information_management/information_management.html',{
        'is_superuser': home_view.is_superuser
    })