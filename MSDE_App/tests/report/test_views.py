from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Report, TypeReport, PhilanthropyMember, Donor, Student


class ReportIntegrationTestCase(TestCase):

    def setUp(self):
        TypeReport.objects.create(
            type_report_code='1234',
            type_report_name='Bienestar'
        )
        type_report = TypeReport.objects.get(type_report_code='1234')
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
        report_code='A00381962',
        report_date='2022-05-10',
        type_report_code=type_report,
        student_code=student,
        philanthropy_member=philanthropyMember
        )

    def test_create_report_through_view(self):
        # Datos de ejemplo para crear un reporte
        report_data = {
            'report_code': 'A00381969',
            'report_date': '2022-05-10',
            'type_report_code': 121,  # Reemplaza con el valor correcto
            'student_code': 123,  # Reemplaza con el valor correcto
            'philanthropy_member': 12345  # Reemplaza con el valor correcto
        }

        # Realiza una solicitud POST para crear el reporte
        response = self.client.post(reverse('reports_generate'), data=report_data)

        # Verifica que la solicitud POST fue exitosa (código de respuesta 200)
        self.assertEqual(response.status_code, 200)

        # Verifica si el reporte se creó en la base de datos
        report_exists = Report.objects.filter(report_code='A00381969').exists()
        self.assertTrue(report_exists)
