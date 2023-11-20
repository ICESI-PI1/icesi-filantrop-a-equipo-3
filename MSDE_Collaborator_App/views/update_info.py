from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from MSDE_App.models import Student


# vista para resolver update_info (segun una URL definida)
# si el método es get, quiere decir que desea ir a la página para
# subir el archivo de info. Luego de seleccionar el tipo de info
# se le muestra la página respectiva
# si es POST quiere decir que ya subió el archivo
def update_info(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    print('tipo de info q desea subir:',request.GET.get("info-type-select"))

    if request.method == 'GET':
        return render(request, '../../MSDE_Collaborator_App/templates/update_info/update_info_student.html',
                      {'student': student,
                       'info_type': request.GET.get("info-type-select")})
