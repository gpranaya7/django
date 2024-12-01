from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.scname
    def get_absolute_url(self):
        return reverse('SchoolDetails', kwargs={'pk':self.pk} )
 
class Student(models.Model):
    sname=models.CharField(max_length=100)
    age=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE ,related_name='students')
    def __str__(self):
        return self.sname
    