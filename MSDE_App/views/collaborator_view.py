from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Collaborator
from MSDE_App.forms import CreateCollaborator

def create_collaborator(request):
    if request.method == 'POST':
        form = CreateCollaborator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateCollaborator()
    return render(request, 'collaborator/create_collaborator.html', {'form': form})

def collaborator_detail(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)
    return render(request, 'collaborator/collaborator_detail.html', {
        'collaborator': collaborator
    })


def collaborators_view(request):
    collaborators_list = Collaborator.objects.all()
    return render(request, 'collaborator/collaborators.html', {
        'collaborators': collaborators_list
    })


def edit_collaborator(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)
    if request.method == 'POST':
        form = CreateCollaborator(request.POST, instance=collaborator)
        if form.is_valid():
            form.save()
    else:
        form = CreateCollaborator(instance=collaborator)
    return render(request, 'collaborator/edit_collaborator.html', {'form': form, 'collaborator': collaborator})


def delete_collaborator(request, collaborator_code):
    collaborator = get_object_or_404(Collaborator, collaborator_code=collaborator_code)
    if request.method == 'POST':
        collaborator.delete()
        return redirect('collaborators/')
    return render(request, 'collaborator/delete_collaborator.html', {'collaborator': collaborator})