from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import Donor


class DonorIntegrationTestCase(TestCase):

    def setUp(self):
        Donor.objects.create(donor_code='1', donor_name='patricio')
        Donor.objects.create(donor_code='2', donor_name='patricio2')
        Donor.objects.create(donor_code='3', donor_name='patricio3')

    def test_create_donor_through_view(self):
        donor_data = {
            'donor_code': '12',
            'donor_name': 'John Doe',
        }

        response = self.client.post(reverse('create_donor'), data=donor_data)
        self.assertEqual(response.status_code, 302)
        donor = Donor.objects.get(donor_code='1')
        self.assertEqual(donor.donor_name, 'patricio')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_donor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donor/create_donor.html')
    
    def test_delete_donor(self):
        donor = Donor.objects.get(donor_code='1')
        response = self.client.post(reverse('delete_donor', args=[donor.donor_code]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Donor.objects.filter(donor_code='1').exists())

    def test_edit_donor(self):
        donor = Donor.objects.get(donor_code='1')
        response = self.client.post(reverse('edit_donor', args=[donor.donor_code]),
                                    data={'donor_code': '1',
                                          'donor_name': 'Bob Esponja'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Donor.objects.filter(donor_code='1').exists())
        self.assertTrue(Donor.objects.filter(donor_name='Bob Esponja').exists())


    def test_donor_detail(self):
        donor = Donor.objects.get(donor_code='1')
        response = self.client.get(reverse('donor_detail', args=[donor.donor_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donor/donor_detail.html')
        self.assertEqual(response.context['donor'], donor)
    
    def test_donor_list_view(self):
        response = self.client.get(reverse('donors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donor/donors.html')


    

