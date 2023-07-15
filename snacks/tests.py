from django.test import TestCase
from django.urls import reverse

class TestSnack (TestCase):
    def test_status_code(self):
        url = ""
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
        

    def test_snacks_templates(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'snack_list.html')
        


