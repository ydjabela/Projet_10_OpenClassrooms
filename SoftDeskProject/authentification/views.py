from django.shortcuts import render
from rest_framework.views import APIView
from authentification.serialzers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from authentification.models import User
from rest_framework.decorators import api_view, permission_classes
# users/views.py


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersAPIView(APIView):

    def get(self, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


