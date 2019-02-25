from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
# allowed request methods for this "view"
@api_view(['GET', 'POST', 'PUT'])


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer