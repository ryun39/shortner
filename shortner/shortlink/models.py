from django.db import models
import datetime

# Create your models here.

class Sample(models.Model):
    create_dt = models.DateTimeField(auto_now_add = True)
    orig_url  = models.CharField(max_length=2000)
    redic_url = models.CharField(max_length=2000)
