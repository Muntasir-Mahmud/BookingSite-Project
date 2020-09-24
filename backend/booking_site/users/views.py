from rest_framework import generics

from api import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
