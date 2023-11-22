from django.shortcuts import render, redirect
from MSDE_App.forms import CSVUploadForm, CreateStudent
import csv
from django.shortcuts import render, redirect, get_object_or_404
from MSDE_App.models import Student
from MSDE_App.forms import CreateStudent
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 

def upload_csv(request): 
    form = CSVUploadForm(request.POST, request.FILES)
    if form.is_valid():
        print("Formulario válido")
        # csv_file = request.FILES['csv_file']
        # decoded_file = csv_file.read().decode('utf-8').splitlines()
        # reader = csv.DictReader(decoded_file)
        # for row in reader:
        #     student_form = CreateStudent(row)
        #     if student_form.is_valid():
        #         student_form.save()
    else:
        pass

@login_required()
def import_students(request):

    if request.method == 'POST':
        upload_csv(request)

    return render(request, 'student/import_students.html')
