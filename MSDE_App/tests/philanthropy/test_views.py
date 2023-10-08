from django.test import TestCase
from django.urls import reverse
from MSDE_App.models import PhilanthropyMember


class philanthropyIntegrationTestCase(TestCase):

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


    def test_create_philanthropy_through_view(self):
        philanthropy_data = {
            'philanthropy_member_code': 'A00381962',
            'philanthropy_member_email': 'victor.garzon@hotmail.com',
            'philanthropy_member_name': 'Victor Manuel Garzon'
        }

        response = self.client.post(reverse('create_philanthropy'), data=philanthropy_data)
        self.assertEqual(response.status_code, 200)
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        self.assertEqual(member1.philanthropy_member_name, 'Victor Manuel Garzon')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create_philanthropy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'philanthropy/create_philanthropy.html')

    def test_edit_philanthropy(self):
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        response = self.client.post(
            reverse('philanthropy_edit', args=[member1.philanthropy_member_code]),
            data={
                'philanthropy_member_code': 'A00381962',
                'philanthropy_member_email': 'victor.garzon9043@hotmail.com',
                'philanthropy_member_name': 'Victor Roberto'
            }
        )
        self.assertEqual(response.status_code, 200)
        member1.refresh_from_db()
        self.assertEqual(member1.philanthropy_member_email, 'victor.garzon9043@hotmail.com')
        self.assertEqual(member1.philanthropy_member_name, 'Victor Roberto')

    def test_delete_philanthropy(self):
        member1 = PhilanthropyMember.objects.get(philanthropy_member_code='A00381962')
        response = self.client.post(reverse('delete_philanthropy', args=[member1.philanthropy_member_code]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(PhilanthropyMember.objects.filter(philanthropy_member_code='A00381962').exists())

