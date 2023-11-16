from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import *
from MSDE_App.forms import CreateMessage


def info_dissemination(request):
    return render(request, '../templates/info_dissemination_collaborator/information_dissemination.html')


def send_info(request):
    # creamos el mensaje - se almacena en la DB y devuelve a la misma página de envío de mensajes
    message_to = request.POST.get('message_to')
    content = request.POST.get('message')
    message_from = "collaborator"

    # Creamos el objeto Message con los datos
    msg = Message.objects.create(
        message_to=message_to,
        message_from=message_from,
        message_content=content
    )
    msg.save()

    return redirect('info_dissemination_col')


def show_info(request):
    # ordenamos los mensajes de filantropia, ya que esta es la view de filantropia, donde el
    # primero es el más reciente
    messages = Message.objects.filter(message_to='collaborator').order_by('-message_date')

    return render(request, '../templates/info_dissemination_collaborator/show_information.html', {
        'messages': messages
    })