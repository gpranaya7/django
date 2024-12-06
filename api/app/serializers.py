from rest_framework import serializers
from app.models import *
class EmpDataSerializers(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'