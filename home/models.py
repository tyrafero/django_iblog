from django.db import models

# Create your models here.

class Feedback(models.Model):
    name= models.CharField(max_length=100)
    post= models.CharField(max_length=400)
    image= models.ImageField(upload_to='media')
    comment= models.TextField(blank=True)