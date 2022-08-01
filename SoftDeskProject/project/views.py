from rest_framework.viewsets import ModelViewSet
from project.models import Project, Contributor, Issue, Comment
from project.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from project.permissions import IsAdminAuthenticated, IsAuthor, IsProjectAuthor, IsContributor


class projectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsContributor, IsProjectAuthor]

    def get_queryset(self):
        print(self.request.user.id)
        return Project.objects.filter(author_user__id=self.request.user.id)
