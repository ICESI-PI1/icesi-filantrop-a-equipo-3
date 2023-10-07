from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'user_type']
        widgets = {
            'user_type': forms.widgets.TextInput(attrs={'readonly': 'readonly'})
        }


class CreateStudent(forms.ModelForm):
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


<<<<<<< Updated upstream
=======

class CreateCollaborator(forms.ModelForm):

    class Meta:
        model = Collaborator
        fields = "__all__"
        widgets = {
            'collaborator_code': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_name': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_email': forms.TextInput(attrs={'class': 'form-control'}),


        }


>>>>>>> Stashed changes
class CreateAlert(forms.ModelForm):
    class Meta:
        model = Alert
        exclude = ['alert_code', 'alert_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['alert_description'].widget.attrs['placeholder'] = "Ingrese una descripción"
        self.fields['alert_sender'].widget.attrs['placeholder'] = "Ingrese el emisor de la alarma"


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
