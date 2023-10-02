from django import forms
from .models import Student, Collaborator


class DateInput(forms.DateInput):
    input_type = 'date'


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

class CreateCollaborator(forms.ModelForm):

    class Meta:
        model = Collaborator
        fields = "__all__"
        widgets = {
            'collaborator_code': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_name': forms.TextInput(attrs={'class': 'form-control'}),
            'collaborator_email': forms.TextInput(attrs={'class': 'form-control'}),


        }



