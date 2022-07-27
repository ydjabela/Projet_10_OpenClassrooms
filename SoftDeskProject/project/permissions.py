from rest_framework.permissions import BasePermission, SAFE_METHODS
from . import models


class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_superuser:
            return super().has_permission(request, view)


class IsContributor(BasePermission):
    message = "You're not a contributor of this project"

    def has_permission(self, request, view, ):
        if not view.kwargs:
            contributor = models.Contributor.objects.filter(user__id=request.user.id)
        elif "project_pk" in view.kwargs:
            contributor = models.Contributor.objects.filter(project__id=view.kwargs["project_pk"]).filter(
                user__id=request.user.id)
        else:
            contributor = models.Contributor.objects.filter(project__id=view.kwargs["pk"]).filter(
                user__id=request.user.id)
        if contributor.exists():
            return True
        return False


class IsAuthor(BasePermission):
    message = "You need to be the author in order to modify or delete."

    def has_object_permission(self, request, view, obj):
        if request.method in [SAFE_METHODS, "POST"]:
            return True
        else:
            # Si la method est DELETE/PUT  mais que le contributeur n'est pas l'auteur alors il n'aura pas l'autorisation
            return request.user == obj.user


class IsProjectAuthor(BasePermission):
    message = "You can't modify this project if you're not its author."

    def has_object_permission(self, request, view, obj):
        contributor = models.Contributor.objects.filter(project__id=view.kwargs["pk"]).get(user__id=request.user.id)
        if request.method in SAFE_METHODS:
            return True
        elif contributor.role == "AUTHOR":
            return True
        else:
            return False
