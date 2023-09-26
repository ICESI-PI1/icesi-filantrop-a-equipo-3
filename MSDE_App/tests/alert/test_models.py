from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Alert
from django.utils import timezone


class AlertTestCase(TestCase):

    def setUp(self):
        Alert.objects.create(alert_code='3549', alert_date='2020-04-07')
        Alert.objects.create(alert_code='1234', alert_date='2023-04-07')
        Alert.objects.create(alert_code='6789', alert_date='2012-04-07')

    def test_alert_creation(self):
        alert = Alert.objects.get(alert_code='3549')
        self.assertIsInstance(alert, Alert)
        self.assertEquals(alert.alert_code, '3549')

        alert2 = Alert.objects.get(alert_code='1234')
        self.assertIsInstance(alert2, Alert)
        self.assertEquals(alert2.alert_code, '1234')

        alert3 = Alert.objects.get(alert_code='6789')
        self.assertIsInstance(alert3, Alert)
        self.assertEquals(alert3.alert_code, '6789')

    def test_unique_constrain(self):
        alert = Alert(alert_code='3549', alert_date='2021-03-01')

        with self.assertRaises(IntegrityError):
            alert.save()



