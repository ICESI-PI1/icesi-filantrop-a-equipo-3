from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Alert
from MSDE_App.forms import CreateAlert


def create_alert(request, student_code):
    if request.method == 'POST':
        try:
            form = CreateAlert(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        except ValueError:
            return render(request, 'student/create_alert.html', {
                'form': form,
                'error': 'Please provide valid data'
            })
    else:
        form = CreateAlert()
    return render(request, 'student/create_alert.html', {'form': form})
