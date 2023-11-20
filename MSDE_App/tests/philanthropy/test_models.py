from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import PhilanthropyMember


class PhilanthropyTestCase(TestCase):

    def setUp(self):
        PhilanthropyMember.objects.create(
            philanthropy_member_code='A00381962',
            philanthropy_member_email='victor.garzon@hotmail.com',
            philanthropy_member_name='Victor Manuel Garzon'
        )
        PhilanthropyMember.objects.create(
            philanthropy_member_code='A00381963',
            philanthropy_member_email='dylan.bermudez@hotmail.com',
            philanthropy_member_name='Dylan Bermudez Cardona'
        )
        PhilanthropyMember.objects.create(
            philanthropy_member_code='A00381892',
            philanthropy_member_email='Luis.charria@hotmail.com',
            philanthropy_member_name='Luis Eduardo Charria'
        )

    def test_philanthropy_creation(self):
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        self.assertIsInstance(member1, PhilanthropyMember)
        self.assertEquals(member1.philanthropy_member_name, 'Victor Manuel Garzon')

        member2 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381963')
        self.assertIsInstance(member2, PhilanthropyMember)
        self.assertEquals(member2.philanthropy_member_name, 'Dylan Bermudez Cardona')

        member3 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381892')
        self.assertIsInstance(member3, PhilanthropyMember)
        self.assertEquals(member3.philanthropy_member_name, 'Luis Eduardo Charria')

    #def test_unique_constrain(self):
     #   member1 = PhilanthropyMember(philanthropy_member_code="A00381962", philanthropy_member_name="Juan castillo")
      #  with self.assertRaises(IntegrityError):
       #     member1.save()

    def test_philanthropy_deletion(self):
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        member1.delete()
        with self.assertRaises(member1.DoesNotExist):
            PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')

    def test_philanthropy_str(self):
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        self.assertEquals(member1.__str__(), 'PhilanthropyMember object (11)')
