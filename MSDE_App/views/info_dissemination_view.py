from django.db.models import Case, Value, When, CharField
from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import *


def info_dissemination(request):
    return render(request, '../templates/info_dissemination/information_dissemination.html')


def send_info(request):
    # creamos el mensaje - se almacena en la DB y devuelve a la misma página de envío de mensajes
    message_to = request.POST.get('message_to')
    content = request.POST.get('message')
    message_from = "philanthropy"

    # Creamos el objeto Message con los datos
    # Creamos el objeto Message con los datos
    msg = Message.objects.create(
        message_to=message_to,
        message_from=message_from,
        message_content=content
    )
    msg.save()
    return redirect('info_dissemination')


def show_info(request):
    method = request.method

    if method == "GET":
        # ordenamos los mensajes de filantropia, ya que esta es la view de filantropia, donde el
        # primero es el más reciente
        messages = Message.objects.filter(message_to='philanthropy').order_by('-message_date')

        messages = messages.annotate(
            message_from_updated=Case(When(message_from='Collaborator', then=Value('Colaborador (Admin.)')),
                When(message_from='Collaborator Registro Académico', then=Value('Colaborador Registro Académico')),
                When(message_from='Collaborator Bienestar Universitario',
                     then=Value('Colaborador Bienestar Universitario')),
                When(message_from='Collaborator Director de Programa', then=Value('Colaborador Director de Programa')),
                When(message_from='Collaborator Apoyo Financiero', then=Value('Colaborador Apoyo Financiero')),
                default=Value('message_from'),  # Mantén el valor original si no coincide
                output_field=CharField(),
            )
        )

        return render(request, '../templates/info_dissemination/show_info.html', {
            'messages_no_solved': messages.filter(status=False),
            'messages_solved': messages.filter(status=True)
        })

    else:
        msg_code = request.POST.get('msg_id')
        message = Message.objects.get(id=msg_code)
        message.status = True
        message.save()

        messages = Message.objects.filter(message_to='philanthropy').order_by('-message_date')

        messages = messages.annotate(
            message_from_updated=Case(
                When(message_from='Collaborator Registro Académico', then=Value('Colaborador Registro Académico')),
                When(message_from='Collaborator Bienestar Universitario',
                     then=Value('Colaborador Bienestar Universitario')),
                When(message_from='Collaborator Director de Programa', then=Value('Colaborador Director de Programa')),
                When(message_from='Collaborator Apoyo Financiero', then=Value('Colaborador Apoyo Financiero')),
                default=Value('message_from'),  # Mantén el valor original si no coincide
                output_field=CharField(),
            )
        )

        return render(request, '../templates/info_dissemination/show_info.html', {
            'messages_no_solved': messages.filter(status=False),
            'messages_solved': messages.filter(status=True)
        })
