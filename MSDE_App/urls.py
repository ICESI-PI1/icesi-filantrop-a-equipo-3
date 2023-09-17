from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('create_student/', views.create_student, name="create_student/"),
    path('students/', views.students, name="students/")

]