from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Student, Donor


# Create your tests here.


class StudentTestCase(TestCase):
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
        Student.objects.create(student_code='A0039869',
                               student_id='1011394',
                               student_name='Pablo',
                               student_email='pablo@pablo.com',
                               student_ICFES_score='355',
                               student_birth_date='2016-08-03',
                               student_phone_number='314123',
                               donor_student_code=don)
        Student.objects.create(student_code='A0037129',
                               student_id='100392',
                               student_name='Sara',
                               student_email='sara@sara.com',
                               student_ICFES_score='389',
                               student_birth_date='2019-08-03',
                               student_phone_number='9393',
                               donor_student_code=don)

    def test_student_exist(self):
        juan = Student.objects.get(student_code='A00381190')
        self.assertEquals(juan.student_name, 'Juan Jose')

        pablo = Student.objects.get(student_code='A0039869')
        self.assertEquals(pablo.student_name, 'Pablo')

        sara = Student.objects.get(student_code='A0037129')
        self.assertEquals(sara.student_name, 'Sara')

    def test_student_relationship(self):
        juan = Student.objects.get(student_code='A00381190')
        self.assertEqual(juan.donor_student_code.donor_name, 'patricio')
        self.assertEqual(juan.donor_student_code.donor_code, '1')

        pablo = Student.objects.get(student_code='A0039869')
        self.assertEquals(pablo.donor_student_code.donor_name, 'patricio')
        self.assertEquals(pablo.donor_student_code.donor_code, '1')

        sara = Student.objects.get(student_code='A0037129')
        self.assertEquals(sara.donor_student_code.donor_name, 'patricio')
        self.assertEquals(sara.donor_student_code.donor_code, '1')

    def test_unique_constraint(self):
        student2 = Student(
            student_code="A00381190",
            student_name="Bob",
            student_birth_date="2001-01-01",
            student_id="2222222222",
            student_email="bob@example.com",
            student_phone_number="0987654321",
            student_ICFES_score=600,
            donor_student_code=None
        )
        with self.assertRaises(IntegrityError):
            student2.save()

