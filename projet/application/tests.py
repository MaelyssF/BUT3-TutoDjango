from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):

    # test url page d'accueil
    def test_home_status_code(self):
        response = self.client.get(reverse('home1')) #reverse("home1") permet d'utiliser le nom de l'URL défini dans urls.py
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('home2')) 
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/application/home/Cricri") 
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/application/hom") 
        self.assertEqual(response.status_code, 404)

    # test contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('home1'))
        self.assertContains(response, 'Hello Django !')

        response = self.client.get(reverse('home2'))         
        self.assertContains(response, 'Hello Django !')

        response = self.client.get("/application/home/Cricri") 
        self.assertContains(response, 'Hello Cricri !')


class ContactViewTest(TestCase):

    # test url page de contact
    def test_contact_status_code(self):
        response = self.client.get(reverse('contact')) 
        self.assertEqual(response.status_code, 200)

    # test contenu de la page de contact
    def test_contact_content(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, "<h1>Contactez-nous !</h1><p><a href='mailto:lorem@ipsum.dolor'>Envoyer un email</a></p>")


class AboutViewTest(TestCase):

    # test url page about
    def test_about_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # test contenu de la page about
    def test_about_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "<h1>What about us ?</h1><p>Maelyss FRONTON, étudiante de BUT3 Informatique à l'<a href='https://www.univ-orleans.fr/fr/iut-orleans'>IUT d'Orléans</a><br><i>🎵 What about all the broken happy ever afters? 🎶🎼</i></p>")