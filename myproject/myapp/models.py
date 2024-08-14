from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=600, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    is_superuser = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500,null=True,blank=True)
    status = models.CharField(max_length=500,null=True,blank=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    dob = models.DateField(null=True, blank=True) 
    class Meta:
        managed = True
        db_table = 'userinfo'
