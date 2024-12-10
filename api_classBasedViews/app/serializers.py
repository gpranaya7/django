from app.models import *
from rest_framework import serializers
class productsSerializedObj(serializers.ModelSerializer):
    class Meta:
        model=products
        fields='__all__'