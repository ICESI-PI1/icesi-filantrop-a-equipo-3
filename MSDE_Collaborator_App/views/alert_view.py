from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_App.models import Alert, Student


def alerts_view(request):
    return render(request, '../../MSDE_Collaborator_App/templates/alert/alerts.html')
