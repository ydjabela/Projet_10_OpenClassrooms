from project.models import Project, Contributor, Issue, Comment
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', "user", "project", "permission", "role"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id", "title", "desc", "tag", "priority", "project", "status", "author_user", "assignee_user", "created_time",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "author_user_id", "issue_id", "created_time"]
