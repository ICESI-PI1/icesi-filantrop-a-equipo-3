from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.forms import CustomUserCreationForm
from MSDE_App.models import User


def registrate_user(request):
    method = request.method

    if method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_type = request.POST.get('type')

        if user_type == 'Filantropía':
            user_type = 'Philanthropy'
        else:
            user_type = 'Collaborator'

        user = User.objects.create_user(
            username=username,
            password=pwd,
            user_type=user_type
        )

        user.save()
        return redirect('index')
    else:
        return render(request, 'registration/registrate.html')
