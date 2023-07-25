from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class TestSnack (TestCase):
    def test_status_code(self):
        url = reverse('snacks')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
        

    def test_snacks_templates(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'snack_list.html')

##################################

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ibra',email='ibra@ok.com',
            password='ibra@12345'
        )
        
        self.Snack = Snack.objects.create(
            name = 'test',
            description= "is ok ",
            purchaser = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.Snack),'test')



    def test_detail_view(self):
        url = reverse('snack_details',args=[self.Snack.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'Snack_Detail.html')

#########################################

    def test_create_view(self):
        url = reverse('create_snack')
        data={
            "name": "test_2",
            "purchaser" : self.user.id,
            "description": "bad"
        }

        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'Snack_Detail.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response, reverse('snack_details',args=[2]))

###############################

    def test_delete_view(self):
        url = reverse('delete_snack',args=[2])
        
        response = self.client.post(path=url, follow = True)
        self.assertEqual(len(Snack.objects.all()),1)
####################################

    def test_update_view(self):
        url = reverse('update_snack',args=[2])
        data={
            "name": "test_2",
            "purchaser" : self.user.id,
            "description": "nice"
        }
        response = self.client.post(path=url, follow = True)
        self.assertEqual(len(Snack.objects.all()),1)