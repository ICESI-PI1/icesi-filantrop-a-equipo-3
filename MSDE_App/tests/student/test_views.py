from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Student, Donor


class StudentIntegrationTestCase(TestCase):

    def setUp(self):
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
        Student.objects.create(student_code='A00381199',
                               student_name='Pablo',
                               student_surname='Lopez',
                               student_birth_date='2000-04-07',
                               student_id='12341',
                               student_email='pablo@h.com',
                               student_phone_number='312412',
                               student_ICFES_score='655', donor_student_code=don)

    def test_create_student_through_view(self):
        student_data = {
            'student_code': '21',
            'student_name': 'Jhon ',
            'student_surname': 'Doe',
            'student_birth_date': '1999-04-07',
            'student_id': '1001367985',
            'student_email': 'sw@ws.co',
            'student_phone_number': '3149094450',
            'student_ICFES_score': '421',
            'donor_student_code': '1'
        }

        response = self.client.post(reverse('create_student'), data=student_data)
        self.assertEqual(response.status_code, 302)  # Verifica que se haya redirigido después de la creación
        student = Student.objects.get(student_code='21')
        self.assertEqual(student.student_name, 'Jhon')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/create_student.html')

    def test_delete_student(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.post(reverse('delete_student', args=[student.student_code]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(student_code='A00381190').exists())

    def test_edit_student(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.post(reverse('edit_student', args=[student.student_code]),
                                    data={'student_code': 'A00381190',
                                          'student_name': 'Jhon ',
                                          'student_surname': 'Doe',
                                          'student_birth_date': '1999-04-07',
                                          'student_id': '1001367985',
                                          'student_email': 'sw@ws.co',
                                          'student_phone_number': '3149094450',
                                          'student_ICFES_score': '421',
                                          'donor_student_code': '1'})
        self.assertEqual(response.status_code, 302)

        student = Student.objects.get(student_code='A00381190')
        self.assertEqual(student.student_name, 'Jhon')
        self.assertEqual(student.student_email, 'sw@ws.co')

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', args=['A00381190']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_detail.html')

    def test_student_list_view(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')

    def test_edit_student_view(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.get(reverse('edit_student', args=[student.student_code]),
                                   data={'student_code': 'A00381190',
                                         'student_name': 'Jhon ',
                                         'student_surname': 'Doe',
                                         'student_birth_date': '1999-04-07',
                                         'student_id': '1001367985',
                                         'student_email': 'sw@ws.co',
                                         'student_phone_number': '3149094450',
                                         'student_ICFES_score': '421',
                                         'donor_student_code': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/edit_student.html')

    def test_delete_student_view(self):
        student = Student.objects.get(student_code='A00381190')
        response = self.client.get(reverse('delete_student', args=[student.student_code]))
        self.assertTemplateUsed(response, 'student/delete_student.html')

    def test_students_view_with_no_search_name(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')
        self.assertContains(response, 'Juan Jose')
        self.assertContains(response, 'Pablo')

    def test_students_view_with_search_name(self):
        response = self.client.get(reverse('students'), {'search_name': 'Juan Jose'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')
        self.assertContains(response, 'Juan Jose')
        self.assertNotContains(response, 'Pablo')
    
    def test_students_view_with_name_initial(self):
        response = self.client.get(reverse('students'), {'name_initial': 'J'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')
        self.assertContains(response, 'Juan Jose')
        self.assertNotContains(response, 'Pablo')
    
    def test_students_view_with_surname_initial(self):
        response = self.client.get(reverse('students'), {'surname_initial': 'L'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')
        self.assertContains(response, 'Juan Jose')
        self.assertContains(response, 'Pablo')
    
    def test_student_view_with_surname(self):
        response = self.client.get(reverse('students'), {'surname_initial': 'L'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/students.html')
        self.assertContains(response, 'Juan Jose')
        self.assertContains(response, 'Pablo')

    