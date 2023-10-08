from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_Collaborator_App import *

@login_required
def index(request):
    user = request.user
    if user.user_type == 'Collaborator':
        return render(request, '../../MSDE_Collaborator_App/templates/index.html')
    else:
        return render(request, 'index.html')
