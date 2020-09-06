from django.db import models
from datetime import datetime
from django.utils import timezone


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    realtor_image = models.ImageField( upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank = True)
    phone = models.CharField( max_length=22)
    email = models.EmailField( max_length=254)
    realtor_of_month = models.BooleanField( default = False)
    hire_date =models.DateTimeField(default = timezone.now, blank =  True)

    def __str__(self):
        return self.name

