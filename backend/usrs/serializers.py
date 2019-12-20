from rest_framework import serializers
from .models import Usr

#user serializer

class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usr
        fields = '__all__'