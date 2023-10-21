from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('index_collaborator/', views.index, name="index"),
    path('student_collaborator/<str:student_code>/student_detail', views.student_detail, name='student_detail_colab'),
    path('students_collaborator/', views.students_view, name="students_colab"),
    path('send_info_collaborator/', views.send_info, name="send_info"),
    path('student_collaborator/<int:student_id>/create_alert/', views.create_alert, name='create_alert'),
    path('collaborator/create_collaborator/', views.create_collaborator, name='create_collaborator'),
    path('collaborator/', views.collaborator_view, name='collaborator'),
    path('collaborator/<str:collaborator_code>/collaborator_detail',
         views.collaborator_detail, name='collaborator_detail'),
    path('collaborator/<str:collaborator_code>/edit/',
         views.collaborator_edit, name='collaborator_edit'),
    path('collaborator/<str:collaborator_code>/delete/', views.collaborator_delete, name='delete_collaborator'),
    path('registrate_collaborator/', views.registrate_user, name='registrate_collaborator'),
    path('info_dissemination_collaborator/', views.info_dissemination, name='info_dissemination')
]
