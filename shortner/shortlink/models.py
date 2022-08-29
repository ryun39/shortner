from tkinter import CASCADE
from django.db import models
from accountapp.models import User

import datetime

# Create your models here.
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Sample(models.Model):
    create_dt = models.DateTimeField(auto_now_add = True)
    orig_url  = models.CharField(max_length=2000)
    redic_url = models.CharField(max_length=2000)

class UserShortenList(TimeStampedModel):
    user_id     = models.ForeignKey('accountapp.User', on_delete=models.CASCADE)
    shorten_url = models.CharField(max_length=2000, blank=False)
    origin_url  = models.CharField(max_length=2000, blank=False)
