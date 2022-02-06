from rest_framework import serializers
from hack.models import BaseModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        
