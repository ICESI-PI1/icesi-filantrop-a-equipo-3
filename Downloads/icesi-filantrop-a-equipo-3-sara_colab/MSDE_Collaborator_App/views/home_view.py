from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from MSDE_Collaborator_App import views

is_superuser = False

@login_required
def index(request):
    global is_superuser
    is_superuser = views.home_view.is_superuser

    render_to_string('../../MSDE_Collaborator_App/templates/layouts/base_collaborator.html', {
        'is_superuser': is_superuser
    })

    return render(request, 'index.html')
