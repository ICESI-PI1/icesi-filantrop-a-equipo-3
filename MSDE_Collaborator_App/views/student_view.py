from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from MSDE_App.models import Student, ExtraAcademic, CreaQuery, AcademicBalance


def student_detail(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    return render(request, 'student/student_detail_collaborator.html', {
        'student': student
    })


def students_view(request):
    students_list = Student.objects.all()

    return render(request, 'student/students_collaborator.html', {
            'students': students_list
        })
