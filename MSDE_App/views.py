from django.shortcuts import render, redirect
from .models import Student
from .forms import CreateStudent


# Create your views here.


def index(request):
    title = "Django course !!"
    return render(request, 'index.html', {
        'title': title
    })


def create_student(request):
    if request.method == 'GET':
        return render(request, 'create_student.html', {
            'form': CreateStudent()
        })
    else:
        Student.objects.create(student_name=request.POST["name"],
                               student_id=request.POST["id"],
                               student_code=request.POST["code"],
                               student_email=request.POST["email"],
                               student_birth_date=request.POST["birth_date"],
                               student_ICFES_score=request.POST["ICFES_score"],
                               student_phone_number=request.POST["phone_number"])
        return redirect('index')


def students(request):
    students = Student.objects.all()
    return render(request, 'students.html',{
        'students': students
    })