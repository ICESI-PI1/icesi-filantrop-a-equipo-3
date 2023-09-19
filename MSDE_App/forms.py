from django import forms
from .models import Student


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateStudent(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),

        }



