from rest_framework.permissions import BasePermission, SAFE_METHODS
from project.models import Project, Contributor, Issue, Comment
from . import models


class IsContributor(BasePermission):
    message = "You're not a contributor of this project"

    def has_permission(self, request, view):
        user_id = request.user.id
        if request.resolver_match.kwargs:
            try:
                project_id = int(request.resolver_match.kwargs["project_id"])
            except KeyError:
                project_id = int(request.resolver_match.kwargs["pk"])
            print(project_id)
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                message = "Project does'nt exist"
                return False
            print(project.id)
            if project.author_user_id == user_id:
                return True
            try:
                contributor = Contributor.objects.get(project__id=project_id, user__id=user_id)
                if contributor.user_id == user_id:
                    print(contributor.user_id, user_id)
                    return True
                else:
                    print(contributor.user_id, project.author_user_id, user_id)
                    return False
            except Contributor.DoesNotExist:
                message = "contributor does'nt exist"
                print(message)
                return False

        else:
            return True


class IsProjectAuthor(BasePermission):
    message = "You're not a author of this project"

    def has_permission(self, request, view):
        user_id = request.user.id
        if request.resolver_match.kwargs:
            try:
                project_id = int(request.resolver_match.kwargs["project_id"])
            except KeyError:
                project_id = int(request.resolver_match.kwargs["pk"])
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                message = "Project does'nt exist"
                print(message)
                return False

            if project.author_user_id == user_id:
                return True
            else:
                return False
        else:
            return True
