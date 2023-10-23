from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_Collaborator_App import *
from django.template.loader import render_to_string

is_superuser = False

@login_required
def index(request):
    user = request.user

    global is_superuser
    is_superuser = user.is_superuser

    if user.user_type == 'Collaborator':
        return redirect("index_col")
    else:
        return render(request, 'index.html')
