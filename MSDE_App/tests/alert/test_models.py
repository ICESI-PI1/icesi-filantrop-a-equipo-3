from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Alert, TypeAlert
from django.utils import timezone


class AlertTestCase(TestCase):

    def setUp(self):

        type2 = TypeAlert.objects.get(alert_type='Bienestar')
        Alert.objects.create(alert_code='1', alert_date='2020-04-07', alert_description='Esto es una alerta',
                             alert_sender='Juan', type_alert=type2)
        Alert.objects.create(alert_code='2', alert_date='2023-04-07', alert_description='Esto es una alerta',
                             alert_sender='Pablo', type_alert=type2)
        Alert.objects.create(alert_code='3', alert_date='2012-04-07', alert_description='Esto es una alerta',
                             alert_sender='Tutu', type_alert=type2)

    def test_alert_creation(self):
        alert = Alert.objects.get(alert_sender='Juan')
        self.assertIsInstance(alert, Alert)
        self.assertEquals(alert.alert_sender, 'Juan')

        alert2 = Alert.objects.get(alert_sender='Pablo')
        self.assertIsInstance(alert2, Alert)
        self.assertEquals(alert2.alert_sender, 'Pablo')

        alert3 = Alert.objects.get(alert_sender='Tutu')
        self.assertIsInstance(alert3, Alert)
        self.assertEquals(alert3.alert_sender, 'Tutu')

    def test_unique_constrain(self):
        type2 = TypeAlert.objects.get(alert_type='Bienestar')

        with self.assertRaises(IntegrityError):
            Alert.objects.create(alert_code='1', alert_date='2020-04-07', alert_description='Esto es una alerta',
                                 alert_sender='Juan', type_alert=type2)
            alert = Alert(alert_code='1', alert_date='2020-04-07', alert_description='Esto es una alerta',
                          alert_sender='Juan', type_alert=type2)
            alert.save()

    def test_alert_relationship(self):
        alert1 = Alert.objects.get(alert_code='1')
        self.assertEquals(alert1.type_alert.alert_type, 'Bienestar')

        alert2 = Alert.objects.get(alert_code='2')
        self.assertEquals(alert2.type_alert.alert_type, 'Bienestar')

        alert3 = Alert.objects.get(alert_code='3')
        self.assertEquals(alert3.type_alert.alert_type,'Bienestar')



    
