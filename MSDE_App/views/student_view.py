from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import CreateStudent
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    title = "Django course !!"
    return render(request, 'index.html', {
        'title': title
    })



def create_student(request):
    if request.method == 'POST':
        form = CreateStudent(request.POST, request.FILES)  
        if form.is_valid():
            student=form.save(commit=False)
            student.save()
            return redirect('index')
        else:
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


def students_view(request):
    students_list = Student.objects.all()
    return render(request, 'student/students.html', {
        'students': students_list
    })


def edit_student(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    
    if request.method == 'POST':
        form = CreateStudent(request.POST, request.FILES, instance=student) 
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_code=student.student_code) 
    else:
        form = CreateStudent(instance=student)
    
    context = {'form': form, 'student': student}
    return render(request, 'student/edit_student.html', context)


def delete_student(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    if request.method == 'POST':
        student.delete()
        return redirect('students')
    return render(request, 'student/delete_student.html', {'student': student})
