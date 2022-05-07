from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Mobile_No= models.CharField(max_length=10)
    is_verified = models.IntegerField( default="0")
    otp= models.CharField(max_length=6)
    Date_of_birth = models.DateField()

