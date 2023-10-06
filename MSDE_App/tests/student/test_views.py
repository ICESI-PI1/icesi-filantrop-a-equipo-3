from django.test import TestCase, Client
from django.urls import reverse
from MSDE_App.models import Student, Donor
from MSDE_App.views import students_view, create_student
from MSDE_App.forms import CreateStudent


class StudentIntegrationTestCase(TestCase):

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

    def test_create_student_through_view(self):
        student_data = {
            'student_code': '12',
            'student_name': 'John Doe',
            'student_birth_date': '2000-01-01',
            'student_id': '12345',
            'student_email': 'john.doe@example.com',
            'student_phone_number': '555-555-5555',
            'student_ICFES_score': 85,
            'donor_student_code': 1,
        }

        response = self.client.post(reverse('create_student'), data=student_data)
        self.assertEqual(response.status_code, 302)  # Verifica que se haya redirigido después de la creación
        student = Student.objects.get(student_code='12')
        self.assertEqual(student.student_name, 'John Doe')

    #def test_view_uses_correct_template(self):
       # response = self.client.get(reverse('create_student'))
       # self.assertEqual(response.status_code, 200)
       # self.assertTemplateUsed(response, 'student/create_student.html')

    def test_delete_student(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.post(reverse('delete_student', args=[student.student_code]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(student_code='A00381190').exists())

    def test_edit_student(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.post(reverse('edit_student', args=[student.student_code]),
                                    data={'student_code': 'A00381190',
                                          'student_id': '1001367985',
                                          'student_name': 'Juan Jose 2',
                                          'student_email': 'juan2@juan2.com',
                                          'student_ICFES_score': '421',
                                          'student_birth_date': '2020-04-07',
                                          'student_phone_number': '3149094450',
                                          'donor_student_code': '1'})
        self.assertEqual(response.status_code, 302)

        student = Student.objects.get(student_code='A00381190')
        self.assertEqual(student.student_name, 'Juan Jose 2')
        self.assertEqual(student.student_email, 'juan2@juan2.com')