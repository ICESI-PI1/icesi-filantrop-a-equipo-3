from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from MSDE_App.models import Alert, Student
from MSDE_App.forms import CreateAlert, AlertFilterForm
from django.contrib import messages


class AlertDetailView(View):
    def get(self, request, alert_code):
        alert = get_object_or_404(Alert, alert_code=alert_code)
        return render(request, 'alert/alert_detail.html', {'alert': alert})

    def post(self, request, alert_code):
        alert = get_object_or_404(Alert, alert_code=alert_code)
        alert.status = True
        alert.save()
        no_solved_alerts = Alert.objects.filter(status=False)
        solved_alerts = Alert.objects.filter(status=True)
        return render(request, 'alert/alerts.html',
                      {'no_solved_alerts': no_solved_alerts, 'solved_alerts': solved_alerts})


class AlertListView(View):
    def get(self, request):
        no_solved_alerts = Alert.objects.filter(status=False)
        solved_alerts = Alert.objects.filter(status=True)
        return render(request, 'alert/alerts.html',
                      {'no_solved_alerts': no_solved_alerts, 'solved_alerts': solved_alerts})


class CreateAlertView(View):
    def get(self, request, student_code):
        student = get_object_or_404(Student, student_code=student_code)
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
                return redirect('create_alert', student_code=student_code)

        return render(request, 'student/create_alert.html', {
            'form': form,
            'student': student,
            'alerts': alerts,
            'filter_form': filter_form
        })
