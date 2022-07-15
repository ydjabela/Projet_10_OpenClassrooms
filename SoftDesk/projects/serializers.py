from projects.models import Project
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']


