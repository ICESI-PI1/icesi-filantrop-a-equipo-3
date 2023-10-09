from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import CreateStudent
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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
            student = form.save(commit=False)
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

    search_name = request.GET.get('search_name', '')
    if search_name:
        students_list = students_list.filter(student_name__icontains=search_name)

    name_initial = request.GET.get('name_initial')
    if name_initial:
        students_list = students_list.filter(student_name__istartswith=name_initial)

    surname_initial = request.GET.get('surname_initial')
    if surname_initial:
        students_list = students_list.filter(student_surname__istartswith=surname_initial)
    elif not surname_initial and not name_initial and not search_name:
        students_list = students_list.order_by('student_surname')

    paginator = Paginator(students_list, 10)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'student/students.html', {
        'students': students
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
