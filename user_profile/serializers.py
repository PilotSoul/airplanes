from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = self.validated_data['password']
        if password != validated_data['password2']:
            raise serializers.ValidationError({'error': 'P1 and P2 are not the same'})
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        # e = User.objects.select_related("customuser").get(id=validated_data.pop("user"))
        # print(e)
        # validated_data["user"] = e
        user = CustomUser.objects.create(**validated_data)
        return user

