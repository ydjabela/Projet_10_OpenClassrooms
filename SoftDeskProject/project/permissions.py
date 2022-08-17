from rest_framework.permissions import BasePermission
from project.models import Project, Contributor, Issue, Comment


class IsContributor(BasePermission):
    message = "You're not a contributor of this project"

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
                return False
            if project.author_user_id == user_id:
                return True
            try:
                contributor = Contributor.objects.get(project__id=project_id, user__id=user_id)
                if contributor.user_id == user_id:
                    return True
                else:
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


class IsIssueAuthor(BasePermission):
    message = "You're not a author of this Issue"

    def has_permission(self, request, view):
        user_id = request.user.id
        if request.resolver_match.kwargs:
            try:
                issue_id = int(request.resolver_match.kwargs["Issue_id"])
            except KeyError:
                issue_id = int(request.resolver_match.kwargs["pk"])
            try:
                issue = Issue.objects.get(id=issue_id)
            except Issue.DoesNotExist:
                message = "Issue does'nt exist"
                print(message)
                return False

            if issue.author_user_id == user_id:
                return True
            else:
                return False
        else:
            return True


class IsCommentAuthor(BasePermission):
    message = "You're not a author of this Comment"

    def has_permission(self, request, view):
        user_id = request.user.id
        if request.resolver_match.kwargs:
            try:
                comment_id = int(request.resolver_match.kwargs["Comment_id"])
            except KeyError:
                comment_id = int(request.resolver_match.kwargs["pk"])
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                message = "Comment does'nt exist"
                print(message)
                return False

            if comment.author_user_id == user_id:
                return True
            else:
                return False
        else:
            return True
