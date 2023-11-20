# Create your models here.
from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# UserManager contiene funciones de creacion de usuarios, lo hacemos para
# manipular el form de registro y los datos a registrar
class UserManager(BaseUserManager):
    def create_user(self, username, password, user_type, **extra_fields):
        if not username:
            raise ValueError('El username es obligatorio.')

        user = self.model(username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.first_name = "a"
        user.last_name = "a"
        user.email = "a"
        user.date_joined = datetime.now()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, user_type, **extra_fields):
        user = self.create_user(username, password, user_type, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.first_name = "a"
        user.last_name = "a"
        user.email = "a"
        user.date_joined = datetime.now()
        user.save(using=self._db)
        return user


# creamos nuestra tabla User a partir de AbstractBaseUser para poder manipular de mejor manera
# y crear nuestras propias funciones de creación
class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, null=False)
    user_type = models.CharField(max_length=150, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    date_joined = models.DateTimeField(null=True)
    USERNAME_FIELD = 'username'
    objects = UserManager()

#class User(AbstractUser):
#    user_type = models.CharField(max_length=20)


class Donor(models.Model):
    donor_code = models.CharField(max_length=12, unique=True)
    donor_name = models.CharField(max_length=20)

    def __str__(self):
        return self.donor_code


class Student(models.Model):
    student_code = models.CharField(max_length=9, unique=True)
    student_name = models.CharField(max_length=24)
    student_surname = models.CharField(max_length=24, null=True)
    student_birth_date = models.DateField(max_length=10)
    student_id = models.CharField(max_length=10)
    student_email = models.CharField(max_length=50)
    student_phone_number = models.CharField(max_length=12)
    student_ICFES_score = models.IntegerField()
    donor_student_code = models.ForeignKey(Donor, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='student_pictures/', null=True, blank=True)

    def __str__(self):
        return self.student_name + "\n" + self.student_code


class ExtraAcademic(models.Model):
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE)
    extra_academic_name = models.CharField(max_length=100)
    extra_academic_hours = models.IntegerField()


class AcademicBalance(models.Model):
    student_code = models.OneToOneField(Student, on_delete=models.CASCADE)
    academic_balance_career = models.CharField(max_length=50)
    academic_balance_subjects = models.CharField(max_length=50)
    academic_balance_schedule = models.CharField(max_length=50)
    academic_balance_additions = models.CharField(max_length=50)
    academic_balance_cancellations = models.CharField(max_length=50)
    academic_balance_semester_average = models.FloatField()
    academic_balance_total_average = models.FloatField()


class CreaQuery(models.Model):
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE)
    crea_query_date = models.DateField()
    crea_query_info = models.CharField(max_length=500)


class TypeReport(models.Model):
    BECA = 'Informe de becas'
    CREA = 'Informe de consultas en el CREA'
    EXTRA = 'Informe de actividades extra académicas'
    PERSONALIZADO = 'Informe personalizado'

    REPORT_TYPE_CHOICES = [
        (BECA, 'Informe de becas'),
        (CREA, 'Informe de consultas en el CREA'),
        (EXTRA, 'Informe de actividades extra académicas'),
        (PERSONALIZADO, 'Informe personalizado')
    ]

    report_type = models.CharField(
        max_length=50,
        choices=REPORT_TYPE_CHOICES,
        unique=True,
        null=True
    )


class PhilanthropyMember(models.Model):
    philanthropy_member_code = models.CharField(max_length=10, unique=True)
    philanthropy_member_name = models.CharField(max_length=24)
    philanthropy_member_email = models.CharField(max_length=50, default="example@gmail.com")


class Report(models.Model):
    report_date = models.DateField(max_length=10)
    type_report_code = models.ForeignKey(TypeReport, on_delete=models.CASCADE)
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE)
    philanthropy_member = models.ForeignKey(PhilanthropyMember, on_delete=models.CASCADE, null=True)


class Collaborator(models.Model):
    collaborator_code = models.CharField(max_length=10, unique=True)
    collaborator_name = models.CharField(max_length=24)
    collaborator_email = models.CharField(max_length=24)

    # adicion de tipo de colaborador
    BIENESTAR_UNIVERSITARIO = 'Bienestar Universitario'
    REGISTRO_ACADEMICO = 'Registro Académico'
    DIRECTOR_PROGRAMA = 'Director de Programa'
    APOYO_FINANCIERO = 'Apoyo Financiero'

    COLLABORATOR_TYPE_CHOICES = [
        (BIENESTAR_UNIVERSITARIO, 'Bienestar Universitario'),
        (REGISTRO_ACADEMICO, 'Registro Académico'),
        (DIRECTOR_PROGRAMA, 'Director de Programa'),
        (APOYO_FINANCIERO, 'Apoyo Financiero')
    ]

    collaborator_type = models.CharField(
        max_length=30,
        choices=COLLABORATOR_TYPE_CHOICES,
        unique=False,
        null=False
    )


class TypeCollaborator(models.Model):
    type_collaborator_code = models.CharField(max_length=10, unique=True)
    type_collaborator_name = models.CharField(max_length=24)


class TypeAlert(models.Model):
    ACADEMICA = 'Académica'
    BIENESTAR = 'Bienestar'
    FINANCIERO = 'Financiero'

    ALERT_TYPE_CHOICES = [
        (ACADEMICA, 'Académica'),
        (BIENESTAR, 'Bienestar'),
        (FINANCIERO, 'Financiero'),
    ]

    alert_type = models.CharField(
        max_length=12,
        choices=ALERT_TYPE_CHOICES,
        unique=True,
        null=True
    )
    def __str__(self):
        return self.alert_type + "\n"


class Alert(models.Model):
    alert_code = models.CharField(max_length=9, unique=True, primary_key=True)
    alert_date = models.DateTimeField(auto_now_add=True, null=True)
    alert_description = models.TextField(blank=True)
    alert_sender = models.CharField(max_length=100, blank=True)
    type_alert = models.ForeignKey(TypeAlert, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)


class Message(models.Model):
    message_from = models.CharField(max_length=12)
    message_to = models.CharField(max_length=12)
    message_content = models.CharField(max_length=3000)
    message_date = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField(default=False)
