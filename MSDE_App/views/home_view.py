from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_Collaborator_App import *
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password

is_superuser = False


def makepwd(request):
    password = "integrador"
    hashed_password = make_password(password)
    print(hashed_password)
    return render(request, 'index.html')

@login_required
def index(request):
    user = request.user

    global is_superuser
    is_superuser = user.is_superuser

    if 'Collaborator' in user.user_type:
        return redirect("index_col")
    else:
        return render(request, 'index.html')
