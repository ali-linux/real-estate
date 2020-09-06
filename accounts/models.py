from django.db import models
from datetime import datetime
from django.utils import timezone


class password_reset(models.Model):
    user_email = models.CharField(max_length=50)
    user_token = models.CharField(max_length=50)
    date_request = models.DateTimeField(default=timezone.now, blank=True)
