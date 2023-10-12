from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_App.models import *

@login_required
def index(request): # pragma: no cover
    return render(request, 'index.html')

