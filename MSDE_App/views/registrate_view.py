from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from MSDE_App.forms import CustomUserCreationForm
from MSDE_App.models import User


class RegistratUserView(View):
    def get(self, request):
        return render(request, 'registration/registrate.html')

    def post(self, request):
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