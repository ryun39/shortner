from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DateOfBirth = models.DateField(null=True)      # 생년월일
    Gender      = models.CharField(max_length=2)   # 성별
    Contact     = models.CharField(max_length=12)  # 연락처
    Payplan     = models.CharField(max_length=2)   # 유료가입
    Period      = models.DateField(null=True, blank=True) # 유료가입 기간
