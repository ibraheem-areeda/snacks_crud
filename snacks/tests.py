from django.test import SimpleTestCase
from django.urls import reverse

class TestSnacks(SimpleTestCase):
    def test_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snacks_templates(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'snack_list.html')


