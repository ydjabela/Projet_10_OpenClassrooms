from rest_framework import viewsets, generics, status, renderers, response, permissions
from project.models import Project, Contributor, Issue, Comment
from project.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from project.permissions import IsAdminAuthenticated, IsProjectAuthor, IsContributor


class projectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsContributor, IsProjectAuthor]

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated()]

        if self.request.method == "GET":
            permission_classes = [
                IsProjectAuthor(),
                permissions.IsAuthenticated(),
            ]
        elif self.request.method == "DELETE" or self.request.method == "PUT":
            permission_classes = [IsProjectAuthor(), permissions.IsAuthenticated()]

        return permission_classes

    def get_queryset(self):
        return Project.objects.filter(author_user__id=self.request.user.id)


class ContributorsListCreateView(generics.ListCreateAPIView):
    """
    List and add contributors to a specific project.
    """

    serializer_class = ContributorSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "project_id"

    def get_queryset(self):
        project_id = self.kwargs.get(self.lookup_field)
        return Contributor.objects.filter(
            project__id__iexact=project_id
        ).prefetch_related("user")

    def create(self, request, *args, **kwargs):

        user_id = request.data["user_id"]
        project_id = kwargs[self.lookup_field]
        permission = request.data["permission"]
        role = request.data["role"]
        serializer = ContributorSerializer(
            data={"user": user_id, "project": project_id, "permission": permission, "role": role}
        )
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return response.Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContributorSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "contributor_id"

    def delete(self, request, *args, **kwargs):
        project_id = kwargs["project_id"]
        contributor_id = kwargs[self.lookup_field]
        try:
            instance = Contributor.objects.get(project__id=project_id, user__id=contributor_id)
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
