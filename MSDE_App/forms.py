from django import forms
from .models import Student
from .models import Alert


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

class CreateAlert(forms.ModelForm):

    class Meta:
        model = Alert
        fields = "__all__"
        widgets = {
            'alert_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'alert_code': forms.TextInput(attrs={'class': 'form-control'}),
            'alert_description': forms.TextInput(attrs={'class': 'form-control'}),
            'alert_sender': forms.TextInput(attrs={'class': 'form-control'}),


        }



