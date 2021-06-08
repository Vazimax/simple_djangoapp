from django.db import models
from datetime import datetime

class Computers(models.Model):

    categories = [
        ('desktop' , 'desktop'),
        ('laptob' , 'laptob'),
    ]

    make = models.CharField(max_length=100)
    config = models.TextField(max_length=9999,default="CPU : \nGPU : \nRAM : ")
    price = models.DecimalField(max_digits=10,decimal_places=3)
    image = models.ImageField(upload_to='images/%y/%m/%d',default="images/21/06/06/sfd.jpeg",null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True,choices=categories)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Computer'
        #ordering = ['make']

    def __str__(self):
        return self.make

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)