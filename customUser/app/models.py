from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
# Create your models here.




class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is not given')
        nemail=self.normalize_email(email)
        uo=self.model(email=nemail,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()  
        return uo
    def create_superuser(self,email,first_name,last_name,password):
        suo=self.create_user(email,first_name,last_name,password)
        suo.is_staff=True
        suo.is_superuser=True
        suo.save()



class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']


