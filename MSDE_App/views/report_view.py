from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from MSDE_App.models import Report
from MSDE_App.forms import *
import itertools
import  pdfkit

#config = pdfkit.configuration(wkhtmltopdf = r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


def download_PDF(request, who):
    if 'extra' in who:
        pdf = pdfkit.from_url(request.build_absolute_uri(reverse('extra_report')))


def base_reports(request):
    return render(request, 'reports_base/base_reports.html')


def becas_report(request):
    return render(request, 'reports_base/becas_report.html')


def extra_report(request):
    return render(request, 'reports_base/actividades_extra_report.html')


def crea_report(request):
    return render(request, 'reports_base/consultas_CREA_report.html')


# views.py
from django.http import HttpResponse

student_list = []
actual_student = None


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


def query_student_crea(request, student_code):
    crea_queries = CreaQuery.objects.filter(student_code=student_code)

    return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': student_list,
                'crea_queries': crea_queries
            })


def query_student_extra(request, student_code):
    crea_queries = ExtraAcademic.objects.filter(student_code=student_code)

    return render(request, 'reports_base/actividades_extra_report.html', {
        'students': student_list,
        'extra': crea_queries
    })


def query_student_becas(request, student_code):
    crea_queries = AcademicBalance.objects.filter(student_code=student_code)

    return render(request, 'reports_base/becas_report.html', {
        'students': student_list,
        'academic_balance': crea_queries
    })


def show_modal(request):
    return render(request, 'report/reports.html', {
        'modal': "true"
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


def report_generate(request):
    report_type = request.GET.get("report-type")

    print('report type:',report_type)

    if report_type is None:
        return render(request, 'report/reports.html', {
            'students': student_list,
        })
    else:
        if report_type == "0":
            return render(request, 'report/reports.html', {
                'students': student_list,
            })
        elif report_type == "1":
            return render(request, 'reports_base/becas_report.html', {
                'students': student_list,
            })
        elif report_type == "2":
            return render(request, 'reports_base/actividades_extra_report.html', {
                'students': student_list,
            })
        elif report_type == "3":
            return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': student_list,
            })
        elif report_type == "4":
            return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': student_list,
            })
        else:
            return render(request, 'report/reports.html', {
                'students': student_list
            })