from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Report, Student, PhilanthropyMember, Donor, TypeReport


class reportTestCase(TestCase):

    def setUp(self):
        TypeReport.objects.create(
            report_type='1',

        )
        type_report = TypeReport.objects.get(report_type='1')
        PhilanthropyMember.objects.create(
            philanthropy_member_code='A00381963',
            philanthropy_member_email='dylan.bermudez@hotmail.com',
            philanthropy_member_name='Dylan Bermudez Cardona'
        )
        philanthropyMember = PhilanthropyMember.objects.get(philanthropy_member_code='A00381963')
        Donor.objects.create(donor_code='1', donor_name='patricio')
        don = Donor.objects.get(donor_code='1')
        Student.objects.create(student_code='A00381968',
                           student_id='1001367985',
                           student_name='Juan Jose',
                           student_email='jjuan@juan.com',
                           student_ICFES_score='421',
                           student_birth_date='2020-04-07',
                           student_phone_number='3149094450',
                           donor_student_code=don)
        student = Student.objects.get(student_code='A00381968')
        Report.objects.create(
        report_date='2022-05-10',
        type_report_code= type_report,
        student_code=student,
        philanthropy_member=philanthropyMember
    )

    def test_report_creation(self):
        report = Report.objects.get(report_code='A00381962')
        self.assertIsInstance(report, Report)
        self.assertEquals(report.report_code, 'A00381962')



    def test_report_relationship(self):
        report = Report.objects.get(report_code='A00381962')
        self.assertEquals(report.student_code.student_code, 'A00381968')
        self.assertEquals(report.type_report_code.report_type, '1')
        self.assertEquals(report.philanthropy_member.philanthropy_member_name, 'Dylan Bermudez Cardona')
        self.assertEquals(report.student_code.donor_student_code.donor_name, 'patricio')

    def test_report_exist(self):
        report = Report.objects.get(report_code='A00381962')
        self.assertEquals(report.report_code, 'A00381962')

    def test_unique_constraint(self):
        report = Report(
            report_date='2023-05-10',
            type_report_code=None,
            student_code=None,
            philanthropy_member=None
        )
        with self.assertRaises(IntegrityError):
            report.save()




