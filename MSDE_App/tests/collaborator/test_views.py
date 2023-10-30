from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Collaborator


class CollaboratorIntegrationTestCase(TestCase):

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


    def test_create_collaborator_through_view(self):
        collaborator_data = {
            'collaborator_code': 'A003819623',
            'collaborator_email': 'victor@hotmail.com',
            'collaborator_name': 'Victor Manuel Garzon'
        }

        response = self.client.post(reverse('create_collaborator'), data=collaborator_data)
        self.assertEqual(response.status_code, 302)
        member1 = Collaborator.objects.get(collaborator_code='A003819623')
        self.assertEqual(member1.collaborator_name, 'Victor Manuel Garzon')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('collaborator'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collaborator_col/collaborator.html')


    def test_delete_colaborator(self):
        member1 = Collaborator.objects.get(collaborator_code='A00381962')
        response = self.client.post(reverse('delete_collaborator', args=[member1.collaborator_code]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Collaborator.objects.filter(collaborator_code='A00381962').exists())
    def test_colaborator_detail_view(self):
        response = self.client.get(reverse('collaborator_detail', args=['A00381962']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'collaborator_col/collaborator_detail.html')

    def test_edit_collaborator(self):
        collaborator = Collaborator.objects.get(collaborator_code='A00381962')
        self.assertEqual(collaborator.collaborator_name, 'Victor Manuel Garzon')
        response = self.client.post(reverse('collaborator_edit', args=[collaborator.collaborator_code]),
                                    data={
            'collaborator_code': 'A00381962',
            'collaborator_email': 'victor9043@hotmail.com',
            'collaborator_name': 'Victor Manuel Pierre'
        })
        self.assertEqual(response.status_code, 200)

        collaborator = Collaborator.objects.get(collaborator_code='A00381962')
        self.assertEqual(collaborator.collaborator_name, 'Victor Manuel Pierre')
        self.assertEqual(collaborator.collaborator_email, 'victor9043@hotmail.com')