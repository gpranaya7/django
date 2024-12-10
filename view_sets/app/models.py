from django.db import models

# Create your models here.

class category(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
class products(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    cid=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.pname