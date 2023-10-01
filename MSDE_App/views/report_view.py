from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Report
from MSDE_App.forms import *
import json

student_list = []

def quit_student(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            student_to_delete = data.get('student')

            student_list.remove(student_to_delete)
            return render(request, 'report/reports.html', {
                'students': student_list
            })
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON: ' + str(e)}, status=400)

def add_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_to_add = data.get('student')

            student_list.append(student_to_add)
            return render(request, 'report/reports.html', {
                'students': student_list
            })
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON: ' + str(e)}, status=400)

def reports_view(request):
    if request.method != 'POST':
        print("entro, no POST")
        return render(request, 'report/reports.html', {
            'students':student_list
        })
    else:
        print("entro, POST")
        try:
            data = json.loads(request.body)
            search_by = data.get('search_by')  # Obtiene el valor enviado desde JavaScript
            data_to_search = data.get('data')
            result = None

            if search_by == "Student Code":
                try:
                    student = get_object_or_404(Student, student_code = data_to_search)
                    result = student
                except Student.DoesNotExist:
                    result = None
            elif search_by == "ID":
                try:
                    student = get_object_or_404(Student, student_id = data_to_search)
                    result = student
                except Student.DoesNotExist:
                    result = None
            elif search_by == "Name":
                try:
                    student = get_object_or_404(Student, student_name = data_to_search)
                    result = student
                except Student.DoesNotExist:
                    result = None

            return render(request, 'report/reports.html', {
                'result': result,
                'students': student_list
            })

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error al decodificar JSON: ' + str(e)}, status=400)