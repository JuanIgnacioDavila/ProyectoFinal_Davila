from django.test import TestCase
from django.urls import reverse
from AppProyectoFinal.models import *

# Create your tests here.


class ViewTest(TestCase):
    def test_no_question(self):
        response=self.client.get(reverse('LeerBlog'))
        self.assertAlmostEqual(response.status_code,200)
        self.assertContains(response,'Vibraciones')
    def test2(self):
        response=self.client.get(reverse('About'))
        self.assertAlmostEqual(response.status_code,200)
        self.assertContains(response,'Un poco mas acerca de mi..')

    def test3(self):
        response=self.client.get(reverse('CrearBlog'))
        self.assertAlmostEqual(response.status_code,200)
        self.assertContains(response,'Registro blog:')    


