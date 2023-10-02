from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/create_student/', views.create_student, name='create_student'),
    path('student/<str:student_code>/student_detail', views.student_detail, name='student_detail'),
    path('students/', views.students_view, name="students/"),
    path('student/<str:student_code>/edit/', views.edit_student, name='edit_student'),
    path('student/<str:student_code>/delete/', views.delete_student, name='delete_student'),
    path('collaborator/create_collaborator/', views.create_collaborator, name='create_collaborator'),
    path('collaborator/<str:collaborator_code>/collaborator_detail', views.collaborator_detail, name='collaborator_detail'),
    path('collaborators/', views.collaborators_view, name="collaborators/"),
    path('collaborator/<str:collaborator_code>/edit/', views.edit_collaborator, name='edit_collaborator'),
    path('collaborator/<str:collaborator_code>/delete/', views.delete_collaborator, name='delete_collaborator')


]