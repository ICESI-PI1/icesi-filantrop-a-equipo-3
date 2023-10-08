from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/<str:student_code>/student_detail', views.student_detail, name='student_detail'),
    path('students/', views.students_view, name="students"),
    path('send_information/', views.send_info_view, name="send_info"),
    path('student/<int:student_id>/create_alert/', views.create_alert, name='create_alert')
]
