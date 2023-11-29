from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Selecciona el archivo CSV')


class CreateExtraAcademic(forms.ModelForm):
    class Meta:
        model = ExtraAcademic
        fields = "__all__"
        widgets = {
            'extra_academic_name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'extra_academic_hours': forms.widgets.NumberInput(attrs={'class': 'form-control'})
        }


class CreateAcademicBalance(forms.ModelForm):
    class Meta:
        model = AcademicBalance
        fields = "__all__"
        widgets = {
            'academic_balance_career': forms.widgets.DateInput(attrs={'type': 'date'}),
            'academic_balance_subjects': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'academic_balance_schedule': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'academic_balance_additions': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'academic_balance_cancellations': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'academic_balance_semester_average': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'academic_balance_total_average': forms.widgets.NumberInput(attrs={'class': 'form-control'})
        }


class CreateCreaQuery(forms.ModelForm):
    class Meta:
        model = CreaQuery
        fields = "__all__"
        widgets = {
            'crea_query_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'crea_query_info': forms.widgets.TextInput(attrs={'class':'form-control'})
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_type']
        widgets = {
            'user_type': forms.widgets.TextInput(attrs={'readonly': 'readonly'})
        }


class CreateStudent(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'student_code': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'student_email': forms.TextInput(attrs={'class': 'form-control'}),
            'student_phone_number': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'student_birth_date': 'Nacimiento del estudiante',
            'student_code': 'Código del estudiante',
            'student_name': 'Nombre del estudiante',
            'student_surname': 'Apellido del estudiante',
            'student_id': 'ID del estudiante',
            'student_email': 'Email del estudiante',
            'student_phone_number': 'Número de teléfono del estudiante',
            'student_ICFES_score': 'Puntaje ICFES',
            'donor_student_code': 'Código de donante',
            'profile_picture': 'Foto del estudiante'
        }




class CreateCollaborator(forms.ModelForm):

    class Meta:
        model = Collaborator
        fields = "__all__"
        widgets = {
            'collaborator_code': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_name': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'collaborator_code': 'Código del Colaborador',
            'collaborator_name': 'Nombre del Colaborador',
            'collaborator_email': 'Correo Electrónico del Colaborador',
            'collaborator_type': 'Tipo de colaborador'
        }


class CreateAlert(forms.ModelForm):
    class Meta:
        model = Alert
        exclude = ['alert_code', 'alert_date', 'student']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alert_description'].widget.attrs['placeholder'] = "Ingrese una descripción"
        self.fields['alert_sender'].widget.attrs['placeholder'] = "Ingrese el emisor de la alerta"
        

class CreateDonor(forms.ModelForm):

    class Meta:
        model = Donor
        fields = "__all__"
        widgets = {
            'donor_code': forms.TextInput(attrs={'class': 'form-control'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CreatePhilanthropy(forms.ModelForm):
    class Meta:
        model = PhilanthropyMember
        fields = "__all__"
        widgets = {
            'philanthropy_member_code' : forms.TextInput(attrs={'class': 'form-control'}),
            'philanthropy_member_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'philanthropy_member_email' : forms.TextInput(attrs={'class': 'form-control'}),
            'philanthropy_member_user' : forms.TextInput(attrs={'class': 'form-control'}),
            'philanthropy_member_password' : forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'philanthropy_member_code': 'Código del Miembro de Filantropía',
            'philanthropy_member_name': 'Nombre del Miembro de Filantropía',
            'philanthropy_member_email': 'Correo Electrónico del Miembro de Filantropía',
            'philanthropy_member_user': 'Usuario del Miembro de Filantropía',
            'philanthropy_member_password': 'Contraseña del Miembro de Filantropía'
        }


class AlertFilterForm(forms.Form):
    
    FILTER_CHOICES = (
        ('sel', '--- Selecciona un filtro ---'),
        ('type', 'Tipo de alerta'),
        ('emisor', 'Remitente'),
    )

    ALERT_TYPE_CHOICES = (
        ('', '--- Selecciona un tipo ---'),
        ('Academica', 'Academica'),
        ('Bienestar', 'Bienestar'),
        ('Financiero', 'Financiero'),
    )

    alert_filter = forms.ChoiceField(choices=FILTER_CHOICES, label="Filtrar por")
    filter_value = forms.ChoiceField(choices=ALERT_TYPE_CHOICES, required=False, label="Valor")

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Selecciona el archivo Excel')
