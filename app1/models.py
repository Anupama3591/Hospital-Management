from django.db import models

# Create your models here.

class User1(models.Model):
    name=models.CharField(max_length=355)
    phonenumber=models.IntegerField(max_length=10)
    gender=models.CharField(max_length=10) 
    fee=models.IntegerField(max_length=20)
    condition=models.CharField(max_length=20) 

class User2(models.Model):
    name=models.CharField(max_length=355)
    Phonenumber=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=355)
    message=models.CharField(max_length=355)


    
