from vibe.backend.users.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

#User viewset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.object.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = UserSerializer