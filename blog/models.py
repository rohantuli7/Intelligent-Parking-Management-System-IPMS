from django.db import models
from datetime import datetime,date

# Create your models here.
class userdata(models.Model):
	email = models.CharField(max_length=40)
	username = models.CharField(max_length=20)
	fname= models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	repassword =models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	designation = models.CharField(max_length=20)
	cp=models.CharField(max_length=10)
	address=models.CharField(max_length=50)
	pincode=models.CharField(max_length=6)
	contactno=models.CharField(max_length=10)
	number_plate= models.CharField(max_length = 10)


class finedata(models.Model):
	name = models.CharField(max_length = 40)
	numberplate = models.CharField(max_length = 40)
	fine = models.CharField( max_length = 40)
	image = models.ImageField( upload_to= 'numberplates_images')