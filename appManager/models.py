from django.db import models
from django.contrib.auth.models import AbstractUser
    
class Profile(AbstractUser):
   GENDER = (('homme','HOMME'), ('femme', 'FEMME'))
   id = models.IntegerField(primary_key=True)
   hometown=models.CharField(blank=True, null=True,max_length=200)
   age=models.IntegerField(null=True)
   gender=models.CharField(choices=GENDER, max_length=10,null=True)

