from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from MSDE_App.models import Report
from MSDE_App.forms import *
import itertools
#import  pdfkit

#config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


#def download_PDF(request, who):
#    if 'extra' in who:
#        pdf = pdfkit.from_url(request.build_absolute_uri(reverse('extra_report')))


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

selected_students = []
actual_student = None


# tenemos muchos forms en la misma página y los forms solo pueden ser enviados como "GET" o "POST",
# como debemos solucionarlos con la misma vista entonces lo que haremos es colocarle un input llamado
# 'form' a los formularios, que tendrá como valor un valor que lo identifique, para así cuando se envíe uno
# identifiquemos a partir de la request cuál se envío obteniendo este input y lo podamos resolver
def generate_report(request):
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

            return render(request, 'report/reports.html', {
                'students': students_list,
                'selected_students': selected_students
            })
        else:
            return render(request, 'report/reports.html', {
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

            return render(request, 'report/reports.html', {
                'students': students,
                'selected_students': selected_students
            })

        if form == 'delete_student':
            student_to_delete = Student.objects.get(student_code=student_code)

            for i in range(0, len(selected_students)):
                if selected_students[i] == student_to_delete:
                    selected_students.pop(i)
                    break

            return render(request, 'report/reports.html', {
                'students': students,
                'selected_students': selected_students
            })

    return render(request, 'report/reports.html', {
        'students': students,
        'selected_students': selected_students
    })


#def quit_student(request, student_code):
#    if request.method == 'POST':
#        student_to_delete = None
#
#        for s in selected_students:
#            if s.student_code == student_code:
#                student_to_delete = s

#        selected_students.remove(student_to_delete)
#        return render(request, 'report/reports.html', {
#            'students': selected_students
#        })


#def add_student(request):
#    if request.method == 'POST':
#        selected_students.append(actual_student)
#        return render(request, 'report/reports.html', {
#            'students': selected_students
#        })


def query_student_crea(request, student_code):
    crea_queries = CreaQuery.objects.filter(student_code=student_code)

    return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': selected_students,
                'crea_queries': crea_queries
            })


def query_student_extra(request, student_code):
    crea_queries = ExtraAcademic.objects.filter(student_code=student_code)

    return render(request, 'reports_base/actividades_extra_report.html', {
        'students': selected_students,
        'extra': crea_queries
    })


def query_student_becas(request, student_code):
    crea_queries = AcademicBalance.objects.filter(student_code=student_code)

    return render(request, 'reports_base/becas_report.html', {
        'students': selected_students,
        'academic_balance': crea_queries
    })


#def show_modal(request):
#    return render(request, 'report/reports.html', {
#        'modal': "true"
#    })


#def reports_view(request):
#    search_by = request.GET.get("search-by-select")
#    data_to_search = request.GET.get("data-to-search")

#    if search_by is None and data_to_search is None:
#        return render(request, 'report/reports.html', {
#            'students': selected_students
#        })
#    else:
#        if search_by == "student-code":
#            try:
#                student = get_object_or_404(Student, student_code=data_to_search)
#                result = student
#            except Student.DoesNotExist:
#                result = None
#        elif search_by == "id":
#            try:
#                student = get_object_or_404(Student, student_id=data_to_search)
#                result = student
#            except Student.DoesNotExist:
#                result = None
#        elif search_by == "name":
#            try:
#                student = get_object_or_404(Student, student_name=data_to_search)
#                result = student
#            except Student.DoesNotExist:
#                result = None
#        else:
#            result = None

 #       global actual_student
 #       actual_student = result

 #       return render(request, 'report/reports.html', {
 #           'result': result,
 #           'students': selected_students
 #       })

# generar el reporte: crear la instancia y el PDF para que pueda ser descargado
def report_generate(request):
    report_type = request.GET.get("report-type")
    students = Student.objects.all()

    if report_type is None:
        return render(request, 'report/reports.html', {
            'students': students,
            'selected_students': selected_students
        })
    else:
        if report_type == "0":
            return render(request, 'report/reports.html', {
                'students': students,
                'selected_students': selected_students
            })
        elif report_type == "1":
            create_report(request, "becas")

            becas = []

            for s in selected_students:
                becas.append(BecasReports(student=s, becas=AcademicBalance.objects.filter(student_code=s.id)))

            return render(request, 'reports_base/becas_report.html', {
                'students': becas,
            })
        elif report_type == "2":
            create_report(request, "extra")

            extra = []

            for s in selected_students:
                extra.append(ExtraReports(student=s, extra=ExtraAcademic.objects.filter(student_code=s.id)))

            return render(request, 'reports_base/actividades_extra_report.html', {
                'students': extra,
            })
        elif report_type == "3":
            create_report(request, "CREA")

            crea = []

            for s in selected_students:
                crea.append(QueryReports(student=s, queries=CreaQuery.objects.filter(student_code=s.id)))

            return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': crea,
            })
        elif report_type == "4":
            create_report(request, "personalizado")
            return render(request, 'reports_base/consultas_CREA_report.html', {
                'students': selected_students,
            })
        else:
            return render(request, 'report/reports.html', {
                'students': selected_students
            })

# crear la instancia del reporte
def create_report(request, which_report):
    if "becas" in which_report:
        for s in selected_students:
            report = Report.objects.create(report_date=datetime.today(),
                                           type_report_code=TypeReport.objects.get(report_type='Informe de becas'),
                                           student_code=Student.objects.get(student_code=s.student_code))
            report.save()
    elif "extra" in which_report:
        for s in selected_students:
            report = Report.objects.create(report_date=datetime.today(),
                                           type_report_code=TypeReport.objects.get(report_type='Informe de consultas en el CREA'),
                                           student_code=Student.objects.get(student_code=s.student_code))
            report.save()
    elif "CREA" in which_report:
        for s in selected_students:
            report = Report.objects.create(report_date=datetime.today(),
                                           type_report_code=TypeReport.objects.get(report_type='Informe de actividades extra académicas'),
                                           student_code=Student.objects.get(student_code=s.student_code))
            report.save()
    else:
        for s in selected_students:
            report = Report.objects.create(report_date=datetime.today(),
                                           type_report_code=TypeReport.objects.get(report_type='Informe personalizado'),
                                           student_code=Student.objects.get(student_code=s.student_code))
            report.save()


class BecasReports:
    def __init__(self, student, becas):
        # Atributos de instancia
        self.student = student
        self.becas = becas


class QueryReports:
    def __init__(self, student, queries):
        # Atributos de instancia
        self.student = student
        self.queries = queries


class ExtraReports:
    def __init__(self, student, extra):
        # Atributos de instancia
        self.student = student
        self.extra = extra
