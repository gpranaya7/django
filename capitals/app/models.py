from django.db import models

# Create your models here.
class country(models.Model):
    id=models.IntegerField(null=False)
    name=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return self.name

class capitals(models.Model):
    name=models.OneToOneField(country,on_delete=models.CASCADE)
    capital=models.CharField(max_length=30,null=False,unique=True)
    def __str__(self):
        return self.capital
        