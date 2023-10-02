from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Donor


class DonorTestCase(TestCase):
    def setUp(self):
        Donor.objects.create(
            donor_code="01",
            donor_name="Jhon Doe")
        Donor.objects.create(
            donor_code="02",
            donor_name="Jane Doe")
        Donor.objects.create(
            donor_code="03",
            donor_name="Jhon Smith")
        
    def test_donor_creation(self):
        donor = Donor.objects.get(donor_code="01")
        self.assertIsInstance(donor, Donor)
        self.assertEquals(donor.donor_code, "01")

        donor2 = Donor.objects.get(donor_code="02")
        self.assertIsInstance(donor2, Donor)
        self.assertEquals(donor2.donor_code, "02")

        donor3 = Donor.objects.get(donor_code="03")
        self.assertIsInstance(donor3, Donor)
        self.assertEquals(donor3.donor_code, "03")
    
    def test_unique_constrain(self):
        donor = Donor(donor_code="01", donor_name="Jhon Doe")
        with self.assertRaises(IntegrityError):
            donor.save()
    
    def test_donor_deletion(self):
        donor = Donor.objects.get(donor_code="01")
        donor.delete()
        with self.assertRaises(Donor.DoesNotExist):
            Donor.objects.get(donor_code="01")
    
    def test_donor_update(self):
        donor = Donor.objects.get(donor_code="01")
        donor.donor_name = "Jhon Doe 2"
        donor.save()
        self.assertEquals(donor.donor_name, "Jhon Doe 2")
    
    def test_donor_str(self):
        donor = Donor.objects.get(donor_code="01")
        self.assertEquals(donor.__str__(), "01")
    

            
    
