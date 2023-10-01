from django.test import TestCase
from MSDE_App.models import TypeAlert


class TypeAlertTestCase(TestCase):
    def setUp(self):
        TypeAlert.objects.create(
            type_alert_code="01",
            type_alert_name="Jhon Doe")
        TypeAlert.objects.create(
            type_alert_code="02",
            type_alert_name="Jane Doe")
        TypeAlert.objects.create(
            type_alert_code="03",
            type_alert_name="Jhon Smith")

    def test_type_alert_creation(self):
        type_alert = TypeAlert.objects.get(type_alert_code="01")
        self.assertIsInstance(type_alert, TypeAlert)
        self.assertEquals(type_alert.type_alert_code, "01")

        type_alert2 = TypeAlert.objects.get(type_alert_code="02")
        self.assertIsInstance(type_alert2, TypeAlert)
        self.assertEquals(type_alert2.type_alert_code, "02")

        type_alert3 = TypeAlert.objects.get(type_alert_code="03")
        self.assertIsInstance(type_alert3, TypeAlert)
        self.assertEquals(type_alert3.type_alert_code, "03")

    def test_type_alert_deletion(self):
        type_alert = TypeAlert.objects.get(type_alert_code="01")
        type_alert.delete()
        with self.assertRaises(TypeAlert.DoesNotExist):
            TypeAlert.objects.get(type_alert_code="01")
        
    def test_type_alert_update(self):
        type_alert = TypeAlert.objects.get(type_alert_code="01")
        type_alert.type_alert_name = "Jhon Doe 2"
        type_alert.save()
        self.assertEquals(type_alert.type_alert_name, "Jhon Doe 2")

