from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Alert, TypeAlert, Student, Donor
from django.urls import reverse

class AlertIntegrationTestCase(TestCase):
    def setUp(self):
        TypeAlert.objects.create(alert_type_code='3')
        type = TypeAlert.objects.get(alert_type_code='3')
        Alert.objects.create(alert_code='3549', alert_date='2020-04-07', alert_description='Esto es una alerta',
                             alert_sender='Juan', type_alert=type)
        Alert.objects.create(alert_code='1234', alert_date='2023-04-07', alert_description='Esto es una alerta',
                             alert_sender='Pablo', type_alert=type)
        Alert.objects.create(alert_code='6789', alert_date='2012-04-07', alert_description='Esto es una alerta',
                             alert_sender='Tutu', type_alert=type)
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

    def test_create_alert_through_view(self):
        alert_data = {
            'alert_code': '12',
            'alert_date': '2020-01-01',
            'alert_description': 'Esto es una alerta',
            'alert_sender': 'Juan',
            'type_alert': 1,
        }

        response = self.client.post(reverse('create_alert', args=['A00381190']), data=alert_data)
        self.assertEqual(response.status_code, 302)
        alert = Alert.objects.get(alert_code='12')
        self.assertEqual(alert.alert_sender, 'Juan')
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_alert', args=['A00381190']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/create_alert.html')

   



