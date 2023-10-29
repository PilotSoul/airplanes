from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from .serializers import UserSerializer, RegisterUserSerializer, ProfileUserSerializer


class UsersAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = ProfileUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProfileUserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAirplane(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
