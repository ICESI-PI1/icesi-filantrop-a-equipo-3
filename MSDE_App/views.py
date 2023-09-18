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


def edit_student(request, student_code):
  # get the student object from the database or return a 404 error
  student = get_object_or_404(Student, student_code=student_code)
  # create a form instance with the student data or the request data
  if request.method == 'POST':
    form = CreateStudent(request.POST)
    # validate and save the form data
    if form.is_valid():
      form.save()
      # redirect to a success page or display a success message
  else:
    form = CreateStudent()
  # render a template with the form and the student data
  return render(request, 'edit_student.html', {'form': form, 'student': student})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('edit_student', pk=pk)
    return render(request, 'delete_student.html', {'student': student})
