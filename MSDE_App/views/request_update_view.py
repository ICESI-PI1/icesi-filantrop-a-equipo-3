from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from MSDE_App.models import *
from MSDE_App.models import Student

selected_students = []


# tenemos muchos forms en la misma página y los forms solo pueden ser enviados como "GET" o "POST",
# como debemos solucionarlos con la misma vista entonces lo que haremos es colocarle un input llamado
# 'form' a los formularios, que tendrá como valor un valor que lo identifique, para así cuando se envíe uno
# identifiquemos a partir de la request cuál se envío obteniendo este input y lo podamos resolver
def request_update(request):
    global selected_students
    students = Student.objects.all()
    method = request.method

    # get forms
    if method == 'GET':
        form = request.GET.get('formulario', None)

        # cada form tiene un input hidden, que indica su nombre para saber a qué
        # form está haciendo referencia la request
        if form == 'search_student':
            students_list = Student.objects.all()

            search_name = request.GET.get('search_name', '')
            if search_name:
                students_list = students_list.filter(student_name__icontains=search_name)

            name_initial = request.GET.get('name_initial')
            if name_initial:
                students_list = students_list.filter(student_name__istartswith=name_initial)

            surname_initial = request.GET.get('surname_initial')
            if surname_initial:
                students_list = students_list.filter(student_surname__istartswith=surname_initial)
            elif not surname_initial and not name_initial and not search_name:
                students_list = students_list.order_by('student_surname')

            paginator = Paginator(students_list, 3)
            page_number = request.GET.get('page')
            students_paginator = paginator.get_page(page_number)

            return render(request, 'request_update/request_update.html', {
                'students': students_list,
                'selected_students': selected_students
            })
        else:
            return render(request, 'request_update/request_update.html', {
                'students': students,
                'selected_students': selected_students
            })

    # post forms
    else:
        form = request.POST.get('formulario', None)
        student_code = request.POST.get('student_code', '')

        if form == 'select_student':
            student_to_add = Student.objects.get(student_code=student_code)
            flag = True

            for i in range(0, len(selected_students)):
                if selected_students[i] == student_to_add:
                    flag = False
                    break

            if flag:
                selected_students.append(student_to_add)

            return render(request, 'request_update/request_update.html', {
                'students': students,
                'selected_students': selected_students
            })

        if form == 'delete_student':
            student_to_delete = Student.objects.get(student_code=student_code)

            for i in range(0, len(selected_students)):
                if selected_students[i] == student_to_delete:
                    selected_students.pop(i)
                    break

            return render(request, 'request_update/request_update.html', {
                'students': students,
                'selected_students': selected_students
            })

        # enviamos la solicitud en forma de mensaje
        if form == 'send':
            message_to = request.POST.get('to', '')
            message_from = "philanthropy"
            content = "Solicitud de actualización para los estudiantes: "

            for i in range(0, len(selected_students)):
                print('código estudiante: ',str(selected_students[i].student_code))
                content += f" |    ESTUDIANTE #{i+1} con Código: {str(selected_students[i].student_code)}, Nombre: {str(selected_students[i].student_name)}, ID: {str(selected_students[i].student_id)} |"

            if message_to == "0":
                return render(request, 'request_update/request_update.html', {
                    'students': students,
                    'selected_students': selected_students
                })
            elif message_to == "1":
                message_to = "Collaborator Bienestar Universitario"
            elif message_to == "2":
                message_to = "Collaborator Registro Académico"
            elif message_to == "3":
                message_to = "Collaborator Director de Programa"
            elif message_to == "4":
                message_to = "Collaborator Apoyo Financiero"

            msg = Message.objects.create(
                message_to=message_to,
                message_from=message_from,
                message_content=content
            )

            selected_students = []

            msg.save()
            return render(request, 'request_update/request_update.html', {
                'students': students,
                'selected_students': selected_students
            })

    return render(request, 'request_update/request_update.html', {
        'students': students,
        'selected_students': selected_students
    })
