from django.db import models
from django.db.models.deletion import CASCADE
from authentification.models import User


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=20)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Contributor(models.Model):

    CHOICES_ROLES = (('ad', 'admin'), ('te', 'technicien'), ('cu', 'customer'))
    CHOICES_PERM = (('R', 'read'), ('RW', 'Read_Write'), ('RWD', 'Read_Write_Delete'))
    user = models.ForeignKey(to=User, on_delete=CASCADE)
    project = models.ForeignKey(to=Project(), on_delete=CASCADE)
    permission = models.CharField(max_length=50, choices=CHOICES_PERM)
    role = models.CharField(max_length=20,  choices=CHOICES_ROLES)


class Issue(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project = models.ForeignKey(to=Project(), on_delete=CASCADE, related_name="issues")
    status = models.CharField(max_length=50)
    author_user = models.ForeignKey(to=User, related_name="author_issue", on_delete=CASCADE, blank=True)
    assignee_user = models.ForeignKey(to=User, related_name="assignee", on_delete=CASCADE, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=250)
    author_user = models.ForeignKey(to=User, related_name="author_comment", on_delete=CASCADE, blank=True)
    issue = models.ForeignKey(to=Issue(), related_name="issue", on_delete=CASCADE, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
