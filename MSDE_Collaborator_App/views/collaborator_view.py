from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import *


def create_collaborator(request):
    if request.method == 'POST':
        form = CreateCollaborator(request.POST)

        try:
            if form.is_valid():
                form.save()
                return redirect('/col/registrate')

        except ValueError:
            return render(request.POST, 'collaborator_col/collaborator.html', {
                'form': CreateCollaborator(request.POST),
                'error': 'Please provide valid data'
            })
    else:
        form = CreateCollaborator()
        print('entra')
        return render(request, 'collaborator_col/create_collaborator.html', {'form': form})


def collaborator_view(request):
    collaborator_members = (Collaborator.objects.all())
    return render(request, 'collaborator_col/collaborator.html', {'collaborator_members': collaborator_members})


def collaborator_detail(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)
    return render(request, 'collaborator_col/collaborator_detail.html',
                  {
                      'collaborator': collaborator
                  })


def collaborator_edit(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)

    if request.method == 'POST':
        form = CreateCollaborator(request.POST, instance=collaborator)
        if form.is_valid():
            form.save()
    else:
        form = CreateCollaborator(instance=collaborator)
    return render(request, 'collaborator_col/edit_collaborator.html', {'form': form, 'collaborator': collaborator})


def collaborator_delete(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)

    if request.method == 'POST':
        collaborator.delete()
        return redirect('collaborator')
    else:
        return render(request, 'collaborator_col/delete_collaborator.html', {'collaborator': collaborator})
