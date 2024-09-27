from django.db import models

# Create your models here.

class signup(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
   
class contact(models.Model):
    contact_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
       
   
class login(models.Model):
    VoterID=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
   
class partyregistration(models.Model):
    nameofparty=models.CharField(max_length=100)
    partyleader=models.CharField(max_length=100)
    
    
class result(models.Model):
    partyname=models.CharField(max_length=100)
    candidatename=models.CharField(max_length=100)
    votes=models.CharField(max_length=100)
    
class count(models.Model):
    partyname=models.CharField(max_length=100)
    votecount=models.CharField(max_length=100)
    
   