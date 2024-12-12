from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    pro_pic=models.ImageField()
    def __str__(self):
        return self.address
class weatherData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    temperature=models.DecimalField(max_digits=5,decimal_places=2)
    humidity=models.DecimalField(max_digits=5,decimal_places=2)
    weather=models.CharField(max_length=10)
    speed=models.CharField(max_length=10)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.city