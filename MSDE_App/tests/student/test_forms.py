from django.test import TestCase, Client
from MSDE_App.models import Student, Donor
from MSDE_App.forms import CreateStudent


class StudentFormTest(TestCase):
    def setUp(self):
        donor = Donor.objects.create(donor_code="1", donor_name="Jane Doe")

    def test_form_valid(self):
        don = Donor.objects.get(donor_code=1)
        form_data = {
            "student_code": "S001",
            "student_name": "Alice Lee",
            "student_birth_date": "2005-01-01",
            "student_id": "123456789",
            "student_email": "alice@lee.com",
            "student_phone_number": "1234567890",
            "student_ICFES_score": 450,
            "donor_student_code": don,
        }

        form = CreateStudent(data=form_data)
        self.assertTrue(form.is_valid())
