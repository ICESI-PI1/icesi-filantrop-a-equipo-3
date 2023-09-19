from django.db import models


# Create your models here.
class Student(models.Model):
    student_code = models.CharField(max_length=9, unique=True)
    student_name = models.CharField(max_length=24)
    student_birth_date = models.DateField(max_length=10)
    student_id = models.CharField(max_length=10)
    student_email = models.CharField(max_length=50)
    student_phone_number = models.CharField(max_length=12)
    student_ICFES_score = models.IntegerField()

    def __str__(self):
        return self.student_name+"\n"+self.student_code


class TypeReport(models.Model):
    type_report_code = models.CharField(max_length=12)
    type_report_name = models.CharField(max_length=16)


class PhilanthropyMember(models.Model):
    philanthropy_member_code = models.CharField(max_length=10)
    philanthropy_member_name = models.CharField(max_length=24)


class Report(models.Model):
    report_code = models.CharField(max_length=14)
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
    alert_code = models.CharField(max_length=20)
    alert_date = models.DateField


class TypeAlert(models.Model):
    type_alert_code = models.CharField(max_length=12)
    type_alert_name = models.CharField(max_length=24)


class Donor(models.Model):
    donor_code = models.CharField(max_length=12)
    donor_name = models.CharField(max_length=20)




