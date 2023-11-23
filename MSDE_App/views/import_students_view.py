import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from MSDE_App.forms import CSVUploadForm
from MSDE_App.models import Student, Donor

@login_required
def upload_csv_or_xlsx(request):
    form = CSVUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        file = request.FILES.get('csv_file')
        if file:  
            print(f"Archivo {file.name} subido correctamente. Analizando el archivo...")

            if file.size == 0:
                messages.error(request, 'El archivo está vacío.')
                return redirect('import_students')  

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
                    return redirect('import_students')  
                print(f"llega")
                
                expected_columns = ['student_code', 'student_name','student_surname','student_birth_date','student_id','student_email', 'student_phone_number','student_ICFES_score', 'donor_student_code']
                if not all(column in df.columns for column in expected_columns):
                    print(df.columns)
                    messages.error(request, 'Faltan columnas esperadas en el archivo.')
                    return redirect('import_students') 

                df = df.rename(columns=lambda x: x.strip())
                df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
                df.dropna(subset=expected_columns, inplace=True)

                for _, row in df.iterrows():
                    donor, _ = Donor.objects.get_or_create(donor_code=row['donor_student_code'])
                    Student.objects.update_or_create(
                        student_code=row['student_code'],
                        defaults={
                            'student_name': row['student_name'],
                            'student_surname': row.get('student_surname'),
                            'student_birth_date': pd.to_datetime(row['student_birth_date'], errors='coerce').date() if pd.notnull(row['student_birth_date']) else None,
                            'student_id': row['student_id'],
                            'student_email': row['student_email'],
                            'student_phone_number': row['student_phone_number'],
                            'student_ICFES_score': int(row['student_ICFES_score']),
                            'donor_student_code': donor,
                        }
                    )

                messages.success(request, "Los estudiantes han sido importados correctamente.")

            except Exception as e:
                messages.error(request, f"Error al procesar el archivo: {e}")
                return redirect('import_students')  

    else:
        messages.error(request, 'Hubo un error con el formulario.')
    return render(request, 'student/import_students.html', {'form': form})

@login_required
def import_students(request):
    if request.method == 'POST':
        return upload_csv_or_xlsx(request)
    else:
        return render(request, 'student/import_students.html')
