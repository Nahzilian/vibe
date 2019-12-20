from rest_framework import serializers
from vibe.backend.users.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'