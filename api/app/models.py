from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.ename