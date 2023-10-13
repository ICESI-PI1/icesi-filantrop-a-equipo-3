from django.test import TestCase
from django.db import IntegrityError
from MSDE_App.models import Collaborator


class CollaboratorTestCase(TestCase):

    def setUp(self):
        Collaborator.objects.create(
            collaborator_code='A00381962',
            collaborator_email='victor.garzon@hotmail.com',
            collaborator_name='Victor Manuel Garzon'
        )
        Collaborator.objects.create(
            collaborator_code='A00381963',
            collaborator_email='dylan.bermudez@hotmail.com',
            collaborator_name='Dylan Bermudez Cardona'
        )
        Collaborator.objects.create(
            collaborator_code='A00381892',
            collaborator_email='Luis.charria@hotmail.com',
            collaborator_name='Luis Eduardo Charria'

        )

    def test_philanthropy_creation(self):
        member1 = Collaborator.objects.get(collaborator_code='A00381962')
        self.assertIsInstance(member1, Collaborator)
        self.assertEquals(member1.collaborator_name, 'Victor Manuel Garzon')
        member2 = Collaborator.objects.get(collaborator_code='A00381963')
        self.assertIsInstance(member2, Collaborator)
        self.assertEquals(member2.collaborator_name, 'Dylan Bermudez Cardona')

        member3 = Collaborator.objects.get(collaborator_code='A00381892')
        self.assertIsInstance(member3, Collaborator)
        self.assertEquals(member3.collaborator_name, 'Luis Eduardo Charria')


    def test_collaborator_deletion(self):
        member1 = Collaborator.objects.get(collaborator_code='A00381962')
        member1.delete()
        with self.assertRaises(member1.DoesNotExist):
            Collaborator.objects.get(collaborator_code='A00381962')

    def test_collaborator_str(self):
        member1 = Collaborator.objects.get(collaborator_code='A00381962')
        self.assertEquals(member1.__str__(), 'Collaborator object (1)')