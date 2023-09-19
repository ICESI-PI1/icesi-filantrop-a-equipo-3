from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import CreateStudent


# Create your views here.


def index(request):
    title = "Django course !!"
    return render(request, 'index.html', {
        'title': title
    })


# def create_student(request):
#   if request.method == 'GET':
##      return render(request, 'student/create_student.html', {
#        'form': CreateStudent()
#   })
# else:
#    Student.objects.create(student_name=request.POST["student_name"],
#                          student_id=request.POST["student_id"],
##                         student_code=request.POST["student_code"],
#                      student_email=request.POST["student_email"],
#                      student_birth_date=request.POST["student_birth_date"],
#                      student_ICFES_score=request.POST["student_ICFES_score"],
#                     student_phone_number=request.POST["student_phone_number"])
# return redirect('index')
def create_student(request):
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateStudent()
    return render(request, 'student/create_student.html', {'form': form})


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
