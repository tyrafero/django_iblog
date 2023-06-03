from django.db import models

# Create your models here.

class Feedback(models.Model):
    name= models.CharField(max_length=100)
    post= models.CharField(max_length=400)
    image= models.ImageField(upload_to='media')
    comment= models.TextField()
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    name= models.CharField(max_length=400)
    logo= models.CharField(max_length=100)
    description= models.TextField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name= models.CharField(max_length=400)
    email= models.EmailField(max_length=50)
    subject= models.TextField(blank=True)
    message= models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class Information(models.Model):
    address_1 = models.CharField(max_length= 500)
    address_2 = models.CharField(max_length= 500)
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length= 100)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.address_1
    

