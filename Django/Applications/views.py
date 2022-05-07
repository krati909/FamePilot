from django.shortcuts import render

# Create your views here.
from Applications.models import User
from Applications.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer