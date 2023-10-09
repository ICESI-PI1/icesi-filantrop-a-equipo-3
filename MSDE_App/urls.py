from django.urls import path, include
from . import views
from MSDE_Collaborator_App import views as vwc
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/create_student/', views.create_student, name='create_student'),
    path('student/<str:student_code>/student_detail', views.student_detail, name='student_detail'),
    path('students/', views.students_view, name="students"),
    path('student/<str:student_code>/edit/', views.edit_student, name='edit_student'),
    path('student/<str:student_code>/delete/', views.delete_student, name='delete_student'),
    path('donor/create_donor/', views.create_donor, name='create_donor'),
    path('donor/<str:donor_code>/donor_detail', views.donor_detail, name='donor_detail'),
    path('donors/', views.donor_view, name="donors/"),
    path('donor/<str:donor_code>/edit/', views.edit_donor, name='edit_donor'),
    path('donor/<str:donor_code>/delete/', views.delete_donor, name='delete_donor'),
    path('student/<str:student_code>/create_alert/', views.create_alert, name='create_alert'),
    path('philanthropy/create_philanthropy/', views.create_philanthropy, name='create_philanthropy'),
    path('philanthropy/', views.philanthropy_view, name='philanthropy'),
    path('philanthropy/<str:philanthropy_code>/philanthropy_detail',
         views.philanthropy_detail, name='philanthropy_detail'),
    path('philanthropy/<str:philanthropy_code>/edit/',
         views.philanthropy_edit, name='philanthropy_edit'),
    path('philanthropy/<str:philanthropy_code>/delete/', views.philanthropy_delete, name='delete_philanthropy'),
    path('reports/', views.reports_view, name='reports'),
    path('reports/generate', views.report_generate, name='reports_generate'),
    path('reports/add_student', views.add_student, name='reports_add_student'),
    path('reports/quit_student/<str:student_code>', views.quit_student, name='reports_quit_student'),
    path('reports/base_reports', views.base_reports, name='base_reports'),
    path('reports/pdf/becas', views.becas_report, name='becas_report'),
    path('reports/pdf/extra', views.extra_report, name='extra_report'),
    path('reports/pdf/CREA', views.crea_report, name='crea_report'),
    path('reports/pdf/CREA/<str:student_code>', views.query_student_crea, name='query_student_crea'),
    path('reports/pdf/extra/<str:student_code>', views.query_student_extra, name='query_student_extra'),
    path('reports/pdf/becas/<str:student_code>', views.query_student_becas, name='query_student_becas'),
    path('reports/true', views.show_modal, name='show_modal'),
    path('registrate/', views.registrate_user, name='registrate'),
    path('salir/', views.salir, name='salir'),
    path('alerts/', views.see_alerts, name='alerts'),
    path('alerts/<str:alert_code>', views.alert_detail, name='alert_detail'),
    path('info_management/', views.info_management, name='info_management')
]
