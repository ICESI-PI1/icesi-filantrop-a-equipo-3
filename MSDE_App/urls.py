from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/create_student/', views.create_student, name='create_student'),
    path('student/<str:student_code>/student_detail', views.student_detail, name='student_detail'),
    path('students/', views.students_view, name="students"),
    path('student/<str:student_code>/edit/', views.edit_student, name='edit_student'),
    path('student/<str:student_code>/delete/', views.delete_student, name='delete_student'),
    path('philanthropy/create_philanthropy/', views.create_philanthropy, name='create_philanthropy'),
    path('philanthropy/', views.philanthropy_view, name='philanthropy'),
    path('philanthropy/<str:philanthropy_code>/philanthropy_detail',
         views.philanthropy_detail, name='philanthropy_detail'),
    path('philanthropy/<str:philanthropy_code>/edit/',
         views.philanthropy_edit, name='philanthropy_edit'),
    path('philanthropy/<str:philanthropy_code>/delete/',
         views.philanthropy_delete, name='delete_philanthropy'),
    path('reports/', views.reports_view ,name='reports'),
    path('reports/add_student', views.add_student ,name='reports_add_student')
]