from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Broadworks(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_system = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    jsession = models.CharField(max_length=255)
    bwsession = models.CharField(max_length=255)