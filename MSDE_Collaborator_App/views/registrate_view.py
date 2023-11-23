from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.forms import CustomUserCreationForm
from MSDE_App.models import User


def registrate_user(request):
    method = request.method

    if method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_type = request.POST.get('type')
        # los colaboradores tienen otro tipo
        collaborator_type = request.POST.get('col_type')

        if collaborator_type == '0':
            return render(request, 'registration/registrate_collaborator.html')

        if user_type == 'Filantropía':
            user_type = 'Philanthropy'
        else:
            # para concatenar sin que se añadan paréntesis ni comas, usamos format
            user_type = 'Collaborator {}'.format(collaborator_type)

        user = User.objects.create_user(
            username=username,
            password=pwd,
            user_type=user_type
        )

        user.save()
        return redirect('index_col')
    else:
        return render(request, 'registration/registrate_collaborator.html')
