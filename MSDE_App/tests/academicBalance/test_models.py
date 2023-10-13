from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import AcademicBalance, Student, Donor


class AcademicBalanceTestCase(TestCase):

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
        AcademicBalance.objects.create(
            student_code=student,
            academic_balance_career='Ingenieria',
            academic_balance_additions='Software',
            academic_balance_cancellations=3,
            academic_balance_schedule='Matematicas',
            academic_balance_subjects=12,
            academic_balance_semester_average=4.3,
            academic_balance_total_average=4.7
        )

    def test_AcademicBalance_creation(self):
        member1 = AcademicBalance.objects.get(academic_balance_career='Ingenieria')
        self.assertIsInstance(member1, AcademicBalance)
        self.assertEquals(member1.academic_balance_career, 'Ingenieria')
        self.assertEquals(member1.academic_balance_cancellations, '3')




    def test_collaborator_deletion(self):
        member1 = AcademicBalance.objects.get(academic_balance_career='Ingenieria')
        member1.delete()
        with self.assertRaises(member1.DoesNotExist):
            AcademicBalance.objects.get(academic_balance_career='Ingenieria')

    def test_collaborator_str(self):
        member1 = AcademicBalance.objects.get(academic_balance_career='Ingenieria')
        self.assertEquals(member1.__str__(), 'AcademicBalance object (1)')