from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import *

def create_philanthropy(request):
    if request.method == 'POST':
        form = CreatePhilanthropy(request.POST)

        try:
            if form.is_valid():
                form.save()
                return redirect('index')
        except ValueError:
            return render(request.POST, 'philanthropy/create_philanthropy.html', {
                'form': CreatePhilanthropy(request.POST),
                'error': 'Please provide valid data'
            })
    else:
        form = CreatePhilanthropy()
        return render(request, 'philanthropy/create_philanthropy.html', {'form': form})