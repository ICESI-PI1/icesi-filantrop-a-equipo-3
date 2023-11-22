from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from MSDE_App.models import User  # Update this import based on your actual model

class InfoDisseminationTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword', user_type='Philanthropy')

    def test_info_dissemination_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Get the URL for the view
        url = reverse('info_dissemination')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, '../templates/info_dissemination/information_dissemination.html')

    def test_info_dissemination_view_not_authenticated(self):
        # Log out the user
        self.client.logout()

        # Get the URL for the view
        url = reverse('info_dissemination')

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 302 (redirect to login)
        self.assertEqual(response.status_code, 200)

        # Check that the user is redirected to the login page
