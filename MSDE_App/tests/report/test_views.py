from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Report, TypeReport, PhilanthropyMember, Donor, Student


class ReportIntegrationTestCase(TestCase):

    def setUp(self):
        TypeReport.objects.create(
            report_type='1'
        )
        type_report = TypeReport.objects.get(report_type='1')
        PhilanthropyMember.objects.create(
            philanthropy_member_code='A00381963',
            philanthropy_member_email='dylan.bermudez@hotmail.com',
            philanthropy_member_name='Dylan Bermudez Cardona'
        )
        PhilanthropyMember.objects.create(
            philanthropy_member_code='12345',
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
        Student.objects.create(student_code='12',
                               student_id='1001367985',
                               student_name='Juan Jose',
                               student_email='jjuan@juan.com',
                               student_ICFES_score='421',
                               student_birth_date='2020-04-07',
                               student_phone_number='3149094450',
                               donor_student_code=don)
        student = Student.objects.get(student_code='A00381968')
        Report.objects.create(
            report_code='A00381963',
            report_date='2022-05-10',
            type_report_code=type_report,
            student_code=student,
            philanthropy_member=philanthropyMember
        )


    def test_create_report_through_view(self):
        # Datos de ejemplo para crear un reporte
        report_data = {
            'report_name': 'becas',
            'report_date': '2022-05-10',
            'type_report': 'Informe de becas',
            'student_code': '1234',
            'philanthropy_member': 'A00381963'
        }
        response = self.client.post(reverse('reports_generate'), data=report_data)
        self.assertEqual(response.status_code, 200)

        report_exists = Report.objects.get(report_date = '2022-05-10')
        self.assertEqual(report_exists.type_report_code.report_type,'1')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reports_generate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')
