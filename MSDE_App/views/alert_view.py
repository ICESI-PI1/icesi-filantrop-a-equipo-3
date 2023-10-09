from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Alert, Student
from MSDE_App.forms import CreateAlert, AlertFilterForm
from django.contrib import messages


def alert_detail(request, alert_code):
    alert = Alert.objects.get(alert_code=alert_code)

    return render(request, 'alert/alert_detail.html', {
        'alert': alert
    })

def see_alerts(request):
    alerts = Alert.objects.all()

    return render(request, 'alert/alerts.html', {
        'alerts': alerts
    })


def create_alert(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)

    if request.method == 'POST':
        form = CreateAlert(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.student = student
            alert.save()
            messages.success(request, 'Alerta guardada correctamente.')
            return redirect('create_alert', student_code=student_code)
        else:
            return render(request, 'student/create_alert.html', {
                'form': form,
                'error': 'Please provide valid data'
            })
    else:
        form = CreateAlert()
        alerts = Alert.objects.filter(student=student).order_by('-alert_date')

        filter_form = AlertFilterForm(request.GET or None)
        if filter_form.is_valid():
            filter_type = filter_form.cleaned_data['alert_filter']
            filter_value = filter_form.cleaned_data['filter_value']
            if filter_type == 'type_alert':
                alerts = alerts.filter(type_alert=filter_value)
            elif filter_type == 'emisor':
                alerts = alerts.filter(emisor=filter_value)
            elif filter_type == 'sel':
                return redirect('create_alert', student_id=student_code)

        return render(request, 'student/create_alert.html', {
            'form': form,
            'student': student,
            'alerts': alerts,
            'filter_form': filter_form

        })
