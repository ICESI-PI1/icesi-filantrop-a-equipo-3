from django import forms
from .models import *


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


class CreateStudent(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'student_code': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'student_email': forms.TextInput(attrs={'class': 'form-control'}),
            'student_phone_number': forms.TextInput(attrs={'class': 'form-control'})
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



