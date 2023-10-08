from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from MSDE_App.models import Alert, Student


def student_detail(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    return render(request, 'student/student_detail.html', {
        'student': student
    })


def students_view(request):
    students_list = Student.objects.all()
    return render(request, 'student/students.html', {
        'students': students_list
    })