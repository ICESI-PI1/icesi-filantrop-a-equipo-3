from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Report
from MSDE_App.forms import *
import json
# views.py
from django.http import HttpResponse

student_list = []
actual_student = None


# def jira_webhook(request, student_to_add):
#    if request.method == 'POST':
#        student_list.append(student_to_add)
#        return render(request, 'report/reports.html', {
#            'students': student_list
#        })


def quit_student(request, student_code):
    if request.method == 'POST':
        student_to_delete = None

        for s in student_list:
            if s.student_code == student_code:
                student_to_delete = s

        student_list.remove(student_to_delete)
        return render(request, 'report/reports.html', {
            'students': student_list
        })


def add_student(request):
    if request.method == 'POST':
        student_list.append(actual_student)
        return render(request, 'report/reports.html', {
            'students': student_list
        })


def reports_view(request):
    search_by = request.GET.get("search-by-select")
    data_to_search = request.GET.get("data-to-search")

    if search_by is None and data_to_search is None:
        return render(request, 'report/reports.html', {
            'students': student_list
        })
    else:
        if search_by == "student-code":
            print("entro-student-code")
            try:
                student = get_object_or_404(Student, student_code=data_to_search)
                result = student
            except Student.DoesNotExist:
                result = None
        elif search_by == "id":
            try:
                student = get_object_or_404(Student, student_id=data_to_search)
                result = student
            except Student.DoesNotExist:
                result = None
        elif search_by == "name":
            try:
                student = get_object_or_404(Student, student_name=data_to_search)
                result = student
            except Student.DoesNotExist:
                result = None
        else:
            result = None

        global actual_student
        actual_student = result

        return render(request, 'report/reports.html', {
            'result': result,
            'students': student_list
        })
