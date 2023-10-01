from django.db import models


# Create your models here.


class Donor(models.Model):
    donor_code = models.CharField(max_length=12, unique=True)
    donor_name = models.CharField(max_length=20)

    def __str__(self):
        return self.donor_code


class Student(models.Model):
    student_code = models.CharField(max_length=9, unique=True)
    student_name = models.CharField(max_length=24)
    student_birth_date = models.DateField(max_length=10)
    student_id = models.CharField(max_length=10)
    student_email = models.CharField(max_length=50)
    student_phone_number = models.CharField(max_length=12)
    student_ICFES_score = models.IntegerField()
    donor_student_code = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name + "\n" + self.student_code


class TypeReport(models.Model):
    type_report_code = models.CharField(max_length=12)
    type_report_name = models.CharField(max_length=16)


class PhilanthropyMember(models.Model):
    philanthropy_member_code = models.CharField(max_length=10)
    philanthropy_member_name = models.CharField(max_length=24)


class Report(models.Model):
    report_code = models.CharField(max_length=14, unique=True, auto_created=True)
    report_date = models.DateField(max_length=10)
    type_report_code = models.ForeignKey(TypeReport, on_delete=models.CASCADE)
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE)
    philanthropy_member = models.ForeignKey(PhilanthropyMember, on_delete=models.CASCADE)


class Collaborator(models.Model):
    collaborator_code = models.CharField(max_length=10)
    collaborator_name = models.CharField(max_length=24)
    collaborator_email = models.CharField(max_length=24)
    collaborator_allow_alert = models.CharField(max_length=4)


class TypeCollaborator(models.Model):
    type_collaborator_code = models.CharField(max_length=10)
    type_collaborator_name = models.CharField(max_length=24)


class Alert(models.Model):
    alert_code = models.CharField(max_length=20, unique=True, auto_created=True)
    alert_date = models.DateField
    alert_description = models.TextField(default="Ingrese una descripcion")
    alert_sender = models.CharField(max_length=100, default="Emisor alarma")


class TypeAlert(models.Model):
    type_alert_code = models.CharField(max_length=12)
    type_alert_name = models.CharField(max_length=24)
