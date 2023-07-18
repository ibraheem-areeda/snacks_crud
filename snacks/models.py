from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default="inter description")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('snack_details',args = [self.id])
    


    

