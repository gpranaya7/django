from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=30)
    loc=models.CharField(max_length=30)
    def __str__(self):
        return str(self.deptno)+self.dname

class Emp(models.Model):
    empno=models.CharField(max_length=10,primary_key=True)
    ename=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
    hiredate=models.DateField(auto_now_add=True)
    deptno=models.ForeignKey('Dept',on_delete=models.CASCADE)
    sal=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=4)
    comm=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return self.ename+str(self.empno)

class SalGrade(models.Model):
    grade=models.IntegerField()
    hisal=models.DecimalField(max_digits=10,decimal_places=4)
    lowsal=models.DecimalField(max_digits=10,decimal_places=4)