from django.db import models

# Create your models here.
class bank(models.Model):
    bank_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.bank_name
class branch(models.Model):
    bank_name=models.ForeignKey(bank,on_delete=models.CASCADE)
    ifsc=models.CharField(max_length=100)
    branch_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phno=models.IntegerField()
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    def __str__(self):
        return self.branch_name
