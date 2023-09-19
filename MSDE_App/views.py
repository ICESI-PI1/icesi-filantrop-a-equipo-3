from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import CreateStudent


# Create your views here.


def index(request):
    title = "Django course !!"
    return render(request, 'index.html', {
        'title': title
    })


def create_student(request):
    if request.method == 'POST':
        try:
            form = CreateStudent(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        except ValueError:
            return render(request, 'student/create_student.html', {
                'form': form,
                'error': 'Please provide valid data'
            })
    else:
        form = CreateStudent()
    return render(request, 'student/create_student.html', {'form': form})


def student_detail(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    return render(request, 'student/student_detail.html', {
        'student': student
    })


def students(request):
    students = Student.objects.all()
    return render(request, 'student/students.html', {
        'students': students
    })


def edit_student(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    if request.method == 'POST':
        form = CreateStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = CreateStudent(instance=student)
    return render(request, 'student/edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    if request.method == 'POST':
        student.delete()
        return redirect('students/')
    return render(request, 'student/delete_student.html', {'student': student})
