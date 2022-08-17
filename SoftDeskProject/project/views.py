from rest_framework import (
    viewsets,
    generics,
    status,
    renderers,
    response,
    permissions
)
from project.models import Project, Contributor, Issue, Comment
from project.serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer
)
from project.permissions import (
    IsProjectAuthor,
    IsContributor,
    IsIssueAuthor,
    IsCommentAuthor
)


class projectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        return Project.objects.filter(author_user__id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        connected_user = self.request.user.id
        user_id = connected_user
        title = request.data["title"]
        description = request.data["description"]
        type = request.data["type"]
        serializer = ProjectSerializer(
            data={
                "author_user": user_id,
                "title": title,
                "description": description,
                "type": type
            }
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

    def update(self, request, *args, **kwargs):
        author_user = self.request.user.id
        project_id = int(request.resolver_match.kwargs["pk"])
        title = request.data["title"]
        description = request.data["description"]
        type = request.data["type"]

        partial = kwargs.pop('partial', False)
        try:
            instance = Project.objects.get(id=project_id)
            data = {
                "author_user": author_user,
                "title": title,
                "description": description,
                "type": type
            }
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class ContributorsListCreateView(generics.ListCreateAPIView):
    """
    List and add contributors to a specific project.
    """

    serializer_class = ContributorSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]
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
            data={
                "user": user_id,
                "project": project_id,
                "permission": permission,
                "role": role
            }
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
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]
    lookup_field = "contributor_id"

    def delete(self, request, *args, **kwargs):
        project_id = kwargs["project_id"]
        contributor_id = kwargs[self.lookup_field]
        try:
            instance = Contributor.objects.get(
                project__id=project_id,
                user__id=contributor_id
            )
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class IssuesListCreateView(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    renderer_classes = [renderers.JSONRenderer]

    permission_classes = [permissions.IsAuthenticated, IsContributor]
    lookup_field = "project_id"

    def get_queryset(self):
        project_id = self.kwargs.get(self.lookup_field)
        return Issue.objects.filter(
            project__id__iexact=project_id
        )

    def create(self, request, *args, **kwargs):
        connected_user = self.request.user.id
        project_id = kwargs[self.lookup_field]
        title = request.data["title"]
        desc = request.data["desc"]
        tag = request.data["tag"]
        priority = request.data["priority"]
        status_1 = request.data["status"]
        author_user = connected_user
        assignee_user = request.data["assignee_user"]
        serializer = IssueSerializer(
            data={
                "title": title,
                "desc": desc,
                "tag": tag,
                "priority": priority,
                "project": project_id,
                "status": status_1,
                "author_user": author_user,
                "assignee_user": assignee_user
            }
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


class IssuesRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IssueSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated, IsIssueAuthor]
    lookup_field = "Issue_id"

    def delete(self, request, *args, **kwargs):
        project_id = kwargs["project_id"]
        Issue_id = kwargs[self.lookup_field]
        try:
            instance = Issue.objects.get(id=Issue_id, project__id=project_id)
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        connected_user = self.request.user.id
        project_id = kwargs["project_id"]
        Issue_id = kwargs[self.lookup_field]
        title = request.data["title"]
        desc = request.data["desc"]
        tag = request.data["tag"]
        priority = request.data["priority"]
        status_1 = request.data["status"]
        author_user = connected_user
        assignee_user = request.data["assignee_user"]
        partial = kwargs.pop('partial', False)
        try:
            instance = Issue.objects.get(id=Issue_id, project__id=project_id)
            data = {
                "title": title,
                "desc": desc,
                "tag": tag,
                "priority": priority,
                "project": project_id,
                "status": status_1,
                "author_user": author_user,
                "assignee_user": assignee_user
            }
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated, IsContributor]

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        issue_id = self.kwargs["Issue_id"]
        issued = Issue.objects.get(id=issue_id, project__id__iexact=project_id)
        return Comment.objects.filter(
            issue__id__iexact=issued.id,
        )

    def create(self, request, *args, **kwargs):
        issue_id = kwargs["Issue_id"]
        project_id = self.kwargs.get("project_id")
        try:
            issued = Issue.objects.get(id=issue_id, project__id__iexact=project_id)
            connected_user = self.request.user.id
            description = request.data["description"]
            author_user = connected_user
            serializer = CommentSerializer(
                data={
                    "description": description,
                    "author_user": author_user,
                    "issue": issued.id,
                }
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
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class CommentRetrieveDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    renderer_classes = [renderers.JSONRenderer]
    permission_classes = [permissions.IsAuthenticated, IsCommentAuthor]
    lookup_field = "Comment_id"

    def delete(self, request, *args, **kwargs):
        comment_id = kwargs[self.lookup_field]
        project_id = kwargs["project_id"]
        issue_id = self.kwargs["Issue_id"]
        try:
            issued = Issue.objects.get(id=issue_id, project__id__iexact=project_id)
            instance = Comment.objects.get(id=comment_id, issue__id=issued.id)
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        connected_user = self.request.user.id
        comment_id = kwargs["Comment_id"]
        project_id = kwargs["project_id"]
        issue_id = kwargs["Issue_id"]
        try:
            issued = Issue.objects.get(id=issue_id, project__id__iexact=project_id)
            description = request.data["description"]
            author_user = connected_user
            partial = kwargs.pop('partial', False)
            instance = Comment.objects.get(id=comment_id, issue__id=issued.id)
            data = {
                    "description": description,
                    "author_user": author_user,
                    "issue": issued.id,
                }
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return response.Response(serializer.data)
        except:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
