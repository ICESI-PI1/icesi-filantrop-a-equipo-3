from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import datetime

from MSDE_App.models import Alert, Student, TypeAlert
from MSDE_App.forms import CreateAlert, AlertFilterForm
from django.contrib import messages

counter = 1

def create_alert(request, student_code):
    global counter
    counter = counter + 1
    student = get_object_or_404(Student, student_code=student_code)

    if request.method == 'POST':
        form = CreateAlert(request.POST)
        print('tipo alerta form: ',request.POST.get('alerttype'))
        typeAlert = TypeAlert.objects.filter(alert_type=request.POST.get('alerttype'))

        alert = Alert.objects.create(
            alert_code='000{}'.format(counter),
            alert_date=datetime.now(),
            alert_sender='Colaborador',
            alert_description=request.POST.get('desc'),
            type_alert=typeAlert[0],
            student=student
        )

        alert.save()

        return redirect('create_alert_collaborator', student_code=student_code)
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
                return redirect('create_alert_collaborator', student_code=student_code)

        return render(request, '../../MSDE_Collaborator_App/templates/alert/create_alert.html', {
            'form': form,
            'student': student,
            'alerts': alerts,
            'filter_form': filter_form
        })

