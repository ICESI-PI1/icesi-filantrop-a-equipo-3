from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import *


def create_philanthropy(request):
    if request.method == 'POST':
        form = CreatePhilanthropy(request.POST)

        try:
            if form.is_valid():
                form.save()
                return redirect('/fil/registrate')

        except ValueError:
            return render(request.POST, 'philanthropy/create_philanthropy.html', {
                'form': CreatePhilanthropy(request.POST),
                'error': 'Please provide valid data'
            })
    else:
        form = CreatePhilanthropy()
        print('entra')
        return render(request, 'philanthropy/create_philanthropy.html', {'form': form})


def philanthropy_view(request):
    philanthropy_members = PhilanthropyMember.objects.all()
    return render(request, 'philanthropy/philanthropy.html', {'philanthropy_members': philanthropy_members})


def philanthropy_detail(request, philanthropy_code):
    philanthropy = get_object_or_404(PhilanthropyMember, philanthropy_member_code=philanthropy_code)
    return render(request, 'philanthropy/philanthropy_detail.html',
                  {
                      'philanthropy': philanthropy
                  })


def philanthropy_edit(request, philanthropy_code):
    philanthropy = get_object_or_404(PhilanthropyMember, philanthropy_member_code=philanthropy_code)

    if request.method == 'POST':
        form = CreatePhilanthropy(request.POST, instance=philanthropy)
        if form.is_valid():
            form.save()
    else:
        form = CreateStudent(instance=philanthropy)
    return render(request, 'philanthropy/edit_philanthropy.html', {'form': form, 'philanthropy': philanthropy})


def philanthropy_delete(request, philanthropy_code):
    philanthropy = get_object_or_404(PhilanthropyMember, philanthropy_member_code=philanthropy_code)

    if request.method == 'POST':
        philanthropy.delete()
        return redirect('philanthropy')
    else:
        return render(request, 'philanthropy/delete_philanthropy.html', {'philanthropy': philanthropy})
