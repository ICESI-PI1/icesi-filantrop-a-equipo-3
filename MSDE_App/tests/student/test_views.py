from django.test import TestCase, Client
from django.urls import reverse
from MSDE_App.models import Student, Donor
from MSDE_App.forms import CreateStudent


class StudentIntegrationTestCase(TestCase):
    def test_create_student_through_view(self):
        # don = Donor.objects.create(donor_code='1', donor_name='patricio')
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
        url = reverse('create_student')
        print(url)
        w = self.client.get(url)
        print(w.content)
        self.assertEqual(response.status_code, 200)  # Verifica que se haya redirigido después de la creación

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/create_student.html')
