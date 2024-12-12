from app.models import *

from django import forms
class userForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}

class profileForm(forms.ModelForm):
    class Meta:
        model=user_profile
        fields=['address','pro_pic']
