from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authentification.models import User
from authentification.serializers import UserSerializer


class UsersAPIView(APIView):

    def get(self, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
