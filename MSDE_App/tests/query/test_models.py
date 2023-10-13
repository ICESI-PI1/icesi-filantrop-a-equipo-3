from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import CreaQuery, Student, Donor


class CreaQueryTestCase(TestCase):

    def setUp(self):
        Donor.objects.create(donor_code='1', donor_name='patricio')
        don = Donor.objects.get(donor_code='1')
        Student.objects.create(student_code='A00381190',
                               student_id='1001367985',
                               student_name='Juan Jose',
                               student_email='jjuan@juan.com',
                               student_ICFES_score='421',
                               student_birth_date='2020-04-07',
                               student_phone_number='3149094450',
                               donor_student_code=don)
        student = Student.objects.get(student_code='A00381190')
        CreaQuery.objects.create(
            student_code=student,
            crea_query_date='2023-02-20',
            crea_query_info='Solicitar informacion'

        )
        Donor.objects.create(donor_code='2', donor_name='patricio')
        don = Donor.objects.get(donor_code='2')
        Student.objects.create(student_code='A00381191',
                               student_id='1001367985',
                               student_name='Juan Jose',
                               student_email='jjuan@juan.com',
                               student_ICFES_score='421',
                               student_birth_date='2020-04-07',
                               student_phone_number='3149094450',
                               donor_student_code=don)
        student3 = Student.objects.get(student_code='A00381191')
        CreaQuery.objects.create(
            student_code=student3,
            crea_query_date='2021-02-20',
            crea_query_info='Solicitar informe'

        )
        Donor.objects.create(donor_code='3', donor_name='patricio')
        don = Donor.objects.get(donor_code='3')
        Student.objects.create(student_code='A00381192',
                               student_id='1001367985',
                               student_name='Juan Jose',
                               student_email='jjuan@juan.com',
                               student_ICFES_score='421',
                               student_birth_date='2020-04-07',
                               student_phone_number='3149094450',
                               donor_student_code=don)
        student2 = Student.objects.get(student_code='A00381192')
        CreaQuery.objects.create(
            student_code=student2,
            crea_query_date='2022-02-20',
            crea_query_info='Solicitar reporte'

        )

    def test_query_creation(self):
        member1 = CreaQuery.objects.get(crea_query_info='Solicitar reporte')
        self.assertIsInstance(member1, CreaQuery)
        self.assertEquals(member1.crea_query_info, 'Solicitar reporte')

        member2 = CreaQuery.objects.get(crea_query_info='Solicitar informe')
        self.assertIsInstance(member2, CreaQuery)
        self.assertEquals(member2.crea_query_info, 'Solicitar informe')


    def test_unique_constrain(self):
        member1 = CreaQuery(student_code = Student.objects.get(student_code='A00381192'))
        with self.assertRaises(IntegrityError):
            member1.save()

    def test_query_deletion(self):
        member1 = CreaQuery.objects.get(crea_query_info='Solicitar informe')
        member1.delete()
        with self.assertRaises(member1.DoesNotExist):
            CreaQuery.objects.get(crea_query_info='Solicitar informe')

    def test_query_str(self):
        member1 = CreaQuery.objects.get(crea_query_info='Solicitar informe')
        self.assertEquals(member1.__str__(), 'CreaQuery object (2)')


