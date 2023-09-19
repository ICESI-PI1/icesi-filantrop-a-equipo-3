from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateStudent(forms.Form):
    code = forms.CharField(label="Student's code", max_length=24, widget=forms.TextInput())
    name = forms.CharField(label="Student's name", max_length=40)
    birth_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    id = forms.CharField(label="Student's id", max_length=12)
    email = forms.CharField(label="Student's mail", max_length=40)
    phone_number = forms.CharField(label="Student's phone number", max_length=40)
    ICFES_score = forms.IntegerField()

