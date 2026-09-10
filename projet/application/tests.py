from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):

    # test url page d'accueil
    def test_home_status_code(self):
        print(reverse("home"))
        response = self.client.get(reverse('home')) #reverse("home") permet d'utiliser le nom de l'URL défini dans urls.py
        self.assertEqual(response.status_code, 200)

    # test contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Hello Django !')