from django.test import TestCase
from MSDE_App.models import TypeAlert


class TypeAlertTestCase(TestCase):
    def setUp(self):
        TypeAlert.objects.create(alert_type_code="01")
        TypeAlert.objects.create(alert_type_code="02")
        TypeAlert.objects.create(alert_type_code="03")

    def test_type_alert_creation(self):
        type_alert = TypeAlert.objects.get(alert_type_code="01")
        self.assertIsInstance(type_alert, TypeAlert)
        self.assertEquals(type_alert.alert_type_code, "01")

        type_alert2 = TypeAlert.objects.get(alert_type_code="02")
        self.assertIsInstance(type_alert2, TypeAlert)
        self.assertEquals(type_alert2.alert_type_code, "02")

        type_alert3 = TypeAlert.objects.get(alert_type_code="03")
        self.assertIsInstance(type_alert3, TypeAlert)
        self.assertEquals(type_alert3.alert_type_code, "03")

    def test_type_alert_deletion(self):
        type_alert = TypeAlert.objects.get(alert_type_code="01")
        type_alert.delete()
        with self.assertRaises(TypeAlert.DoesNotExist):
            TypeAlert.objects.get(alert_type_code="01")

