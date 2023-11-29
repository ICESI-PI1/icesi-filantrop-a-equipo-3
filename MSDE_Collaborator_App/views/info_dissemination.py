from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import *

def info_dissemination(request):
    return render(request, '../templates/info_dissemination_collaborator/information_dissemination.html')


def send_info(request):
    # creamos el mensaje - se almacena en la DB y devuelve a la misma página de envío de mensajes
    message_to = request.POST.get('message_to')
    content = request.POST.get('message')
    message_from = request.user.user_type

    # Creamos el objeto Message con los datos
    msg = Message.objects.create(
        message_to=message_to,
        message_from=message_from,
        message_content=content
    )
    msg.save()

    return redirect('info_dissemination_col')


def show_info(request):
    user = request.user
    method = request.method

    if method == "GET":
        # ordenamos los mensajes y hacemos una query de todos los q son para este tipo de colaborador y para todos los colabroadores
        messages = Message.objects.filter(Q(message_to=user.user_type) | Q(message_to='collaborator-all')).order_by(
            '-message_date')

        for i in range(0, len(messages)):
            if 'Solicitud de actualización' in messages[i].message_content:
                mensaje_transformado = messages[i].message_content  # Concatenar las partes
                mensaje_transformado = mensaje_transformado.replace('(', '')  # Quitar paréntesis abiertos
                mensaje_transformado = mensaje_transformado.replace(')', '')  # Quitar paréntesis cerrados
                mensaje_transformado = mensaje_transformado.replace(',', '')  # Quitar comas
                mensaje_transformado = mensaje_transformado.replace('\'', '')  # Quitar comas
                mensaje_transformado = mensaje_transformado.replace('\\n', ''
                                                                           '')  # Reemplazar '\n' con saltos de línea HTML

                messages[i].message_content = mensaje_transformado

        return render(request, '../templates/info_dissemination_collaborator/show_information.html', {
            'messages_no_solved': messages.filter(status=False),
            'messages_solved': messages.filter(status=True)
        })

    else:
        msg_code = request.POST.get('msg_id')
        message = Message.objects.get(id=msg_code)
        message.status = True
        message.save()

        # ordenamos los mensajes y hacemos una query de todos los q son para este tipo de colaborador y para todos los colabroadores
        messages = Message.objects.filter(Q(message_to=user.user_type) | Q(message_to='collaborator-all')).order_by(
            '-message_date')

        for i in range(0, len(messages)):
            if 'Solicitud de actualización' in messages[i].message_content:
                mensaje_transformado = messages[i].message_content  # Concatenar las partes
                mensaje_transformado = mensaje_transformado.replace('(', '')  # Quitar paréntesis abiertos
                mensaje_transformado = mensaje_transformado.replace(')', '')  # Quitar paréntesis cerrados
                mensaje_transformado = mensaje_transformado.replace(',', '')  # Quitar comas
                mensaje_transformado = mensaje_transformado.replace('\'', '')  # Quitar comas
                mensaje_transformado = mensaje_transformado.replace('\\n', ''
                                                                           '')  # Reemplazar '\n' con saltos de línea HTML

                messages[i].message_content = mensaje_transformado

        return render(request, '../templates/info_dissemination_collaborator/show_information.html', {
            'messages_no_solved': messages.filter(status=False),
            'messages_solved': messages.filter(status=True)
        })
