from django.db import models
from authentification.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=20)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
