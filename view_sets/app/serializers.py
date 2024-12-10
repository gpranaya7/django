from rest_framework import serializers
from app.models import *
class SerializedProducts(serializers.ModelSerializer):
    class Meta:
        model=products
        fields='__all__'