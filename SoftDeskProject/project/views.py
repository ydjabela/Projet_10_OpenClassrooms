from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from project.models import Project
from project.serializers import ProjectSerializer
from project.permissions import IsAdminAuthenticated, IsAuthor, IsProjectAuthor


class ProjectsAPIView(APIView):
    permission_classes = [IsAdminAuthenticated, IsProjectAuthor]

    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
