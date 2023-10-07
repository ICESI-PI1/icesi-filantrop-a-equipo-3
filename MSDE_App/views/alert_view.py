from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Alert, Student
from MSDE_App.forms import CreateAlert

<<<<<<< Updated upstream
def create_alert(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
=======

def create_alert(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
>>>>>>> Stashed changes
    
    if request.method == 'POST':
        form = CreateAlert(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)  
            alert.student = student  
            alert.save()  
            return redirect('index')
        else:
            return render(request, 'student/create_alert.html', {
                'form': form,
                'error': 'Please provide valid data'
            })
    else:
        form = CreateAlert()
    
    return render(request, 'student/create_alert.html', {'form': form, 'student': student})
