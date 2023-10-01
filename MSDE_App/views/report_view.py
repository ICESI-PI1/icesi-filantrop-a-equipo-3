from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Report
from MSDE_App.forms import *

student_list = None

def add_student(request, student_to_add):
    if request.method == 'POST':
        student_list.append(student_to_add)
        return render(request, 'report/reports.html', {
            'students':student_list
        })

def reports_view(request):
    if request.method != 'POST':
        return render(request, 'report/reports.html', {
            'students':student_list
        })
    else:
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