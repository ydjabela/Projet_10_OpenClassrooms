from rest_framework.viewsets import ModelViewSet
from project.models import Project, Contributor, Issue, Comment
from project.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from project.permissions import IsAdminAuthenticated, IsProjectAuthor, IsContributor
from rest_framework.permissions import IsAuthenticated


class projectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsContributor, IsProjectAuthor]

    def get_permissions(self):
        permission_classes = [IsAuthenticated()]

        if self.request.method == "GET":
            permission_classes = [
                IsProjectAuthor(),
                IsAuthenticated(),
            ]
        elif self.request.method == "DELETE" or self.request.method == "PUT":
            permission_classes = [IsProjectAuthor(), IsAuthenticated()]

        return permission_classes

    def get_queryset(self):
        return Project.objects.filter(author_user__id=self.request.user.id)
