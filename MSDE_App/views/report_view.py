from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from MSDE_App.models import Report
from MSDE_App.forms import *
import itertools
import  pdfkit

#config = pdfkit.configuration(wkhtmltopdf = r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")


#def download_PDF(request, who):
#    if 'extra' in who:
#        pdf = pdfkit.from_url(request.build_absolute_uri(reverse('extra_report')))


class BaseReportsView(View):
    def get(self, request):
        return render(request, 'reports_base/base_reports.html')

class BecasReportView(View):
    def get(self, request):
        return render(request, 'reports_base/becas_report.html')

class ExtraReportView(View):
    def get(self, request):
        return render(request, 'reports_base/actividades_extra_report.html')

class CreaReportView(View):
    def get(self, request):
        return render(request, 'reports_base/consultas_CREA_report.html')

# views.py
from django.http import HttpResponse

selected_students = []
actual_student = None


# tenemos muchos forms en la misma página y los forms solo pueden ser enviados como "GET" o "POST",
# como debemos solucionarlos con la misma vista entonces lo que haremos es colocarle un input llamado
# 'form' a los formularios, que tendrá como valor un valor que lo identifique, para así cuando se envíe uno
# identifiquemos a partir de la request cuál se envío obteniendo este input y lo podamos resolver
class GenerateReportView(View):
    selected_students = []

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'report/reports.html', {
            'students': students,
            'selected_students': self.selected_students
        })

    def post(self, request):
        form = request.POST.get('formulario', None)
        student_code = request.POST.get('student_code', '')

        if form == 'select_student':
            student_to_add = Student.objects.get(student_code=student_code)
            flag = True

            for i in range(0, len(self.selected_students)):
                if self.selected_students[i] == student_to_add:
                    flag = False
                    break

            if flag:
                self.selected_students.append(student_to_add)

        elif form == 'delete_student':
            student_to_delete = Student.objects.get(student_code=student_code)

            for i in range(0, len(self.selected_students)):
                if self.selected_students[i] == student_to_delete:
                    self.selected_students.pop(i)
                    break

        students = Student.objects.all()
        return render(request, 'report/reports.html', {
            'students': students,
            'selected_students': self.selected_students
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


class QueryStudentCreaView(View):
    def get(self, request, student_code):
        crea_queries = CreaQuery.objects.filter(student_code=student_code)

        return render(request, 'reports_base/consultas_CREA_report.html', {
            'students': GenerateReportView.selected_students,
            'crea_queries': crea_queries
        })

class QueryStudentExtraView(View):
    def get(self, request, student_code):
        crea_queries = ExtraAcademic.objects.filter(student_code=student_code)

        return render(request, 'reports_base/actividades_extra_report.html', {
            'students': GenerateReportView.selected_students,
            'extra': crea_queries
        })

class QueryStudentBecasView(View):
    def get(self, request, student_code):
        crea_queries = AcademicBalance.objects.filter(student_code=student_code)

        return render(request, 'reports_base/becas_report.html', {
            'students': GenerateReportView.selected_students,
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
class ReportGenerateView(View):
    def get(self, request):
        report_type = request.GET.get("report-type")
        students = Student.objects.all()

        if report_type is None:
            return render(request, 'report/reports.html', {
                'students': students,
                'selected_students': GenerateReportView.selected_students
            })
        else:
            if report_type == "0":
                return render(request, 'report/reports.html', {
                    'students': students,
                    'selected_students': GenerateReportView.selected_students
                })
            elif report_type == "1":
                self.create_report(request, "becas")
                return render(request, 'reports_base/becas_report.html', {
                    'students': GenerateReportView.selected_students,
                })
            elif report_type == "2":
                self.create_report(request, "extra")
                return render(request, 'reports_base/actividades_extra_report.html', {
                    'students': GenerateReportView.selected_students,
                })
            elif report_type == "3":
                self.create_report(request, "CREA")
                return render(request, 'reports_base/consultas_CREA_report.html', {
                    'students': GenerateReportView.selected_students,
                })
            elif report_type == "4":
                self.create_report(request, "personalizado")
                return render(request, 'reports_base/consultas_CREA_report.html', {
                    'students': GenerateReportView.selected_students,
                })
            else:
                return render(request, 'report/reports.html', {
                    'students': GenerateReportView.selected_students
                })

    # crear la instancia del reporte

    def create_report(self, request, which_report):
        if "becas" in which_report:
            for s in GenerateReportView.selected_students:
                report = Report.objects.create(report_date=datetime.today(),
                                               type_report_code=TypeReport.objects.get(report_type='Informe de becas'),
                                               student_code=Student.objects.get(student_code=s.student_code))
                report.save()
        elif "extra" in which_report:
            for s in GenerateReportView.selected_students:
                report = Report.objects.create(report_date=datetime.today(),
                                               type_report_code=TypeReport.objects.get(
                                                   report_type='Informe de consultas en el CREA'),
                                               student_code=Student.objects.get(student_code=s.student_code))
                report.save()
        elif "CREA" in which_report:
            for s in GenerateReportView.selected_students:
                report = Report.objects.create(report_date=datetime.today(),
                                               type_report_code=TypeReport.objects.get(
                                                   report_type='Informe de actividades extra académicas'),
                                               student_code=Student.objects.get(student_code=s.student_code))
                report.save()
        else:
            for s in GenerateReportView.selected_students:
                report = Report.objects.create(report_date=datetime.today(),
                                               type_report_code=TypeReport.objects.get(
                                                   report_type='Informe personalizado'),
                                               student_code=Student.objects.get(student_code=s.student_code))
                report.save()

