from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework import generics
from .serializers import CustomUserSerializer

class UsersAPIList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
