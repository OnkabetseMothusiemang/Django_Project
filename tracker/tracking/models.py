from django.db import models

# Create your models here.
class Locations(models.com):
    club = models.CharField(max_length=500,blank=True,null=True)
    name =models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    country = models.CharField(max_length=200,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    created_at = models.CharField(auto_now_add=True,blank=True,null=True)
    edited_at = models.CharField(auto_now_add=True)

    def __str__(self):
      return self.name

    
