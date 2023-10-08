from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import CreaQuery, Student, Donor


class CreaQueryTestCase(TestCase):

    def setUp(self):
        Donor.objects.create(donor_code='1', donor_name='patricio')
        don = Donor.objects.get(donor_code='1')
        student = Student.objects.create(
            student_code='A00381966',
            student_id='1001367985',
            student_name='Juan Jose',
            student_email='jjuan@juan.com',
            student_ICFES_score='421',
            student_birth_date='2020-04-07',
            student_phone_number='3149094450',
            donor_student_code=don
        )
        CreaQuery.objects.create(
            crea_query_date='2023-02-2012',
            crea_query_info='Solicitar'

        )

