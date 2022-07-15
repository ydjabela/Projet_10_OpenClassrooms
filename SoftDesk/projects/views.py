from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectsAPIView(APIView):

    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
