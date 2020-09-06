from django.db import models
from datetime import datetime
from django.utils import timezone

class Contact(models.Model):
    listing = models.CharField( max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField( max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

