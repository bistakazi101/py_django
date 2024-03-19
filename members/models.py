from django.db import models

# Create your models here.
class member(models.Model):  #it means the django should inherit all the properties of the Model class
    firstname= models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
