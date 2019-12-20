from .models import Usr
from rest_framework import viewsets, permissions
from .serializers import UsrSerializer

class UsrViewSet(viewsets.ModelViewSet):
    queryset = Usr.objects.all()
    permissions_classes =  [
        permissions.AllowAny
    ]
    serializer_class = UsrSerializer