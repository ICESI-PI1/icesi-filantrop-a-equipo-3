from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/create_student/', views.create_student, name='create_student'),
    path('student/<str:student_code>/student_detail', views.student_detail, name='student_detail'),
    path('students/', views.students_view, name="students"),
    path('student/<str:student_code>/edit/', views.edit_student, name='edit_student'),
    path('student/<str:student_code>/delete/', views.delete_student, name='delete_student'),
    path('collaborator/create_collaborator/', views.create_collaborator, name='create_collaborator'),
    path('collaborator/<str:collaborator_code>/collaborator_detail', views.collaborator_detail, name='collaborator_detail'),
    path('collaborators/', views.collaborators_view, name="collaborators/"),
    path('collaborator/<str:collaborator_code>/edit/', views.edit_collaborator, name='edit_collaborator'),
    path('collaborator/<str:collaborator_code>/delete/', views.delete_collaborator, name='delete_collaborator'),
    path('student/<str:student_code>/create_alert/', views.create_alert, name='create_alert'),
    path('philanthropy/create_philanthropy/', views.create_philanthropy, name='create_philanthropy'),
    path('philanthropy/', views.philanthropy_view, name='philanthropy'),
    path('philanthropy/<str:philanthropy_code>/philanthropy_detail',
         views.philanthropy_detail, name='philanthropy_detail'),
    path('philanthropy/<str:philanthropy_code>/edit/',
         views.philanthropy_edit, name='philanthropy_edit'),
    path('philanthropy/<str:philanthropy_code>/delete/',
         views.philanthropy_delete, name='delete_philanthropy'),
    path('reports/', views.reports_view, name='reports'),
    path('reports/add_student', views.add_student, name='reports_add_student'),
    path('reports/quit_student/<str:student_code>', views.quit_student, name='reports_quit_student'),
         views.philanthropy_delete, name='delete_philanthropy')
]
