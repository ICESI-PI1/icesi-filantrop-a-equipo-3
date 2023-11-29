
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from MSDE_App.models import Student, ExtraAcademic, CreaQuery, AcademicBalance

#info_to_upload = ''

# vista para resolver update_info (segun una URL definida)
# si el método es get, quiere decir que desea ir a la página para
# subir el archivo de info. Luego de seleccionar el tipo de info
# se le muestra la página respectiva
# si es POST quiere decir que ya subió el archivo
def update_info(request, student_code):
    student = get_object_or_404(Student, student_code=student_code)
    #global info_to_upload
    #info_to_upload = request.GET.get("info-type-select")

    if request.method == 'GET':
        return render(request, '../../MSDE_Collaborator_App/templates/update_info/update_info_student.html',
                      {'student': student,
                       'info_type': request.GET.get("info-type-select")})
    else:
        upload = request.POST.get('upload')

        if request.method == 'POST':
            file = request.FILES.get('csv_file')
            if file:
                print(f"Archivo {file.name} subido correctamente. Analizando el archivo...")

                if file.size == 0:
                    messages.error(request, 'El archivo está vacío.')
                    return redirect('update_info_student', student_code=student_code)

                try:
                    print(f"try")
                    if file.name.endswith('.csv'):
                        try:
                            print(f"archivo csv")
                            df = pd.read_csv(file, encoding='utf-8', dtype=str, delim_whitespace=True)
                        except UnicodeDecodeError:
                            df = pd.read_csv(file, encoding='iso-8859-1', dtype=str)
                    elif file.name.endswith('.xlsx'):
                        print(f"archivo excel")
                        df = pd.read_excel(file, dtype=str)
                    else:
                        messages.error(request, 'Formato de archivo no soportado.')
                        return redirect('update_info_student', student_code=student_code)
                    print(f"llega")
                    print(upload)

                    if df is None:
                        print('es none ??')
                    else:
                        print('no es none')

                    # cada metodo sube el excel de la manera que sea necesaria
                    # dependiendo del tipo
                    if 'extra' in upload:
                        extra_upload(request, df, student_code)
                    elif 'balance' in upload:
                        balance_upload(request, df, student_code)
                    else:
                        crea_upload(request, df, student_code)


                except Exception as e:
                    messages.error(request, f"Error al procesar el archivo: {e}")
                    return redirect('update_info_student', student_code=student_code)

        else:
            messages.error(request, 'Hubo un error con el formulario.')
        return redirect('update_info_student', student_code=student_code)


def balance_upload(request, df, student_code):
    expected_columns = ['academic_balance_career', 'academic_balance_subjects', 'academic_balance_schedule',
                        'academic_balance_additions', 'academic_balance_cancellations', 'academic_balance_semester_average',
                        'academic_balance_total_average', 'student_code']

    print(df)

    if not all(column in df.columns for column in expected_columns):
        print(df.columns)
        messages.error(request, 'Faltan columnas esperadas en el archivo.')
        return redirect('update_info_student', student_code=student_code)

    #df = df.rename(columns=lambda x: x.strip())
    #df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    #df.dropna(subset=expected_columns, inplace=True)

    for _, row in df.iterrows():
        student = Student.objects.get(student_code=row['student_code'])
        academicBalance = AcademicBalance.objects.create(
                academic_balance_career=row['academic_balance_career'],
                academic_balance_subjects=row.get('academic_balance_subjects'),
                academic_balance_schedule=row.get('academic_balance_schedule'),
                academic_balance_additions=row.get('academic_balance_additions'),
                academic_balance_cancellations=row.get('academic_balance_cancellations'),
                academic_balance_semester_average=row.get('academic_balance_semester_average'),
                academic_balance_total_average=row.get('academic_balance_total_average'),
                student_code=student
        )
        academicBalance.save()

    messages.success(request, "Se ha cargado correctamente el balance académico.")


def extra_upload(request, df,student_code):
    expected_columns = ['extra_academic_name', 'extra_academic_hours', 'student_code']

    if not all(column in df.columns for column in expected_columns):
        print(df.columns)
        messages.error(request, 'Faltan columnas esperadas en el archivo.')
        return redirect('update_info_student', student_code=student_code)

    for _, row in df.iterrows():
        print('entra a guardar')
        student = Student.objects.get(student_code=row['student_code'])
        print('estudiante con codigo: ',student.student_code)
        extra = ExtraAcademic.objects.create(
            extra_academic_name=row['extra_academic_name'],
            extra_academic_hours=row.get('extra_academic_hours'),
            student_code=student
        )

        extra.save()

    messages.success(request, "Se ha cargado correctamente el informe extra-académico.")


def crea_upload(request, df,student_code):
    expected_columns = ['crea_query_date', 'crea_query_info', 'student_code']

    if not all(column in df.columns for column in expected_columns):
        print(df.columns)
        messages.error(request, 'Faltan columnas esperadas en el archivo.')
        return redirect('update_info_student', student_code=student_code)

    for _, row in df.iterrows():
        student = Student.objects.get(student_code=row['student_code'])
        crea = CreaQuery.objects.create(
            crea_query_date=pd.to_datetime(row['crea_query_date'],
                                                     errors='coerce').date() if pd.notnull(
                    row['crea_query_date']) else None,
            crea_query_info=row['crea_query_info'],
            student_code=student
        )

        crea.save()

    messages.success(request, "Se ha cargado correctamente el informe de consultas en el CREA.")
