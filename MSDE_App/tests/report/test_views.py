from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Report, TypeReport, PhilanthropyMember, Donor, Student
from MSDE_App.views import report_view


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
        Student.objects.create(student_code='A00381190',
                               student_name='Juan Jose',
                               student_surname='Lopez',
                               student_birth_date='1999-04-07',
                               student_id='1001367985',
                               student_email='juan@h.com',
                               student_phone_number='3149094450',
                               student_ICFES_score='421', donor_student_code=don)
        Student.objects.create(student_code='123',
                               student_name='Pablo',
                               student_surname='Lopez',
                               student_birth_date='2000-04-07',
                               student_id='12341',
                               student_email='pablo@h.com',
                               student_phone_number='312412',
                               student_ICFES_score='655', donor_student_code=don)
        student = Student.objects.get(student_code='A00381190')
        Report.objects.create(
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

        report_exists = Report.objects.get(report_date='2022-05-10')
        self.assertEqual(report_exists.type_report_code.report_type, '1')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('reports_generate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')

    def test_view_uses_correct_template_base(self):
        response = self.client.get(reverse('base_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/base_reports.html')

    def test_view_uses_correct_template_becas(self):
        response = self.client.get(reverse('becas_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/becas_report.html')

    def test_view_uses_correct_template_activi(self):
        response = self.client.get(reverse('extra_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/actividades_extra_report.html')

    def test_view_uses_correct_template_consultas(self):
        response = self.client.get(reverse('crea_report'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/consultas_CREA_report.html')

    def test_query_student_crea(self):
        student = Student.objects.get(student_code='123')
        response = self.client.get(reverse('query_student_crea', args=[student.student_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/consultas_CREA_report.html')

    def test_query_student_becas(self):
        student = Student.objects.get(student_code='123')
        response = self.client.get(reverse('query_student_becas', args=[student.student_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/becas_report.html')

    def test_query_student_extra(self):
        student = Student.objects.get(student_code='123')
        response = self.client.get(reverse('query_student_extra', args=[student.student_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/actividades_extra_report.html')



    def test_reports_with_no_search_data_nor_search_by(self):
        response = self.client.get(reverse('reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')

    def test_reports_view_with_valid_student_code(self):
        response = self.client.get(reverse('reports'),
                                   {'search-by-select': 'student-code', 'data-to-search': 'A00381190'})
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'report/reports.html')

    def test_reports_view_with_valid_search_by_id(self):
        response = self.client.get(reverse('reports'), {'search-by-select': 'id', 'data-to-search': '12341'})
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'report/reports.html')

    def test_reports_view_with_valid_search_by_name(self):
        response = self.client.get(reverse('reports'), {'search-by-select': 'name', 'data-to-search': 'Juan Jose'})
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'report/reports.html')

    def test_reports_view_with_invalid_search_by(self):
        response = self.client.get(reverse('reports'), {'search-by-select': 'invalid', 'data-to-search': 'Juan Jose'})
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'report/reports.html')

    def test_report_generate_no_report_type(self):
        response = self.client.get(reverse('reports_generate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')
    
    def test_report_generate_report_type_0(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')
    
    def test_report_generate_report_type_1(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/becas_report.html')
    
    def test_report_generate_report_type_2(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/actividades_extra_report.html')
    
    def test_report_generate_report_type_3(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/consultas_CREA_report.html')
    
    def test_report_generate_report_type_4(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '4'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports_base/consultas_CREA_report.html')
    
    def test_report_generate_invalid_report_type_5(self):
        response = self.client.get(reverse('reports_generate'), {'report-type': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'report/reports.html')


    