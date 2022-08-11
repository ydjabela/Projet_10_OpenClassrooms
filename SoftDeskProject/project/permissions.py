from rest_framework.permissions import BasePermission, SAFE_METHODS
from project.models import Project, Contributor, Issue, Comment
from . import models


class IsContributor(BasePermission):
    message = "You're not a contributor of this project"

    def has_permission(self, request, view, ):
        if not view.kwargs:
            contributor = Contributor.objects.filter(user__id=request.user.id)
        elif "project_pk" in view.kwargs:
            contributor = Contributor.objects.filter(project__id=view.kwargs["project_pk"]).filter(
                user__id=request.user.id)
        else:
            contributor = Contributor.objects.filter(project__id=view.kwargs["pk"]).filter(
                user__id=request.user.id)
        if contributor.exists():
            return True
        return False


class IsProjectAuthor(BasePermission):
    message = "You're not a author of this project"

    def has_permission(self, request, view):
        user_id = request.user.id
        if request.resolver_match.kwargs:
            try:
                project_id = int(request.resolver_match.kwargs["project_pk"])
            except KeyError:
                project_id = int(request.resolver_match.kwargs["pk"])
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return False

            if project.author_user_id == user_id:
                return True
            else:
                return False
        else:
            return True
