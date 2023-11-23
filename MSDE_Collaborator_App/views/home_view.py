from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from MSDE_Collaborator_App import views

is_superuser = False

@login_required
def index(request):
    return render(request, 'index_collaborator.html')
