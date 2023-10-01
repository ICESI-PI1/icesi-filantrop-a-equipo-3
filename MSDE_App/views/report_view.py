from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Report
from MSDE_App.forms import *


def reports_view(request):
    return render(request, 'report/reports.html')
