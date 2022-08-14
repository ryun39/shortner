from django.db import models

# Create your models here.
class Sample(models.Model):
    orig_url  = models.CharField(max_length=2000)
    redic_url = models.CharField(max_length=2000)
