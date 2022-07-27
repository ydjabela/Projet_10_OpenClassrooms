from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from project.models import Project, Contributor, Issue, Comment
from project.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from project.permissions import IsAdminAuthenticated, IsAuthor, IsProjectAuthor


class ProjectsAPIView(APIView):
    permission_classes = [IsAdminAuthenticated, IsProjectAuthor, IsAuthor]

    def get(self, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Project.objects.filter(contributors__id=self.request.user.id)
        return queryset

    def perform_create(self, serializer_class):
        project = serializer_class.save()
        contributor = Contributor.objects.create(project=project, role="AUTHOR", user=self.request.user)
