from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.forms import CustomUserCreationForm


def registrate_user(request):

    refer = request.META.get('HTTP_REFERER', None)

    if 'philanthropy' in refer:
        user_type = 'Philanthropy'
    elif 'collaborator' in refer:
        user_type = 'Collaborator'
    else:
        user_type = ''

    data = {
        'form': CustomUserCreationForm(initial={'user_type': user_type})
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('index')
    return render(request, 'registration/registrate_collaborator.html', data)
