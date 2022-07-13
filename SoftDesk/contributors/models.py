from django.db import models
from django.db.models.deletion import CASCADE
from authentification.models import User
from projects.models import Project
# Create your models here.


class Contributor(models.Model):

    CHOICES_ROLES = (('ad', 'admin'), ('te', 'technicien'), ('cu', 'customer'))
    CHOICES_PERM = (('R', 'read'), ('RW', 'Read_Write'), ('RWD', 'Read_Write_Delete'))
    user = models.ForeignKey(to=User, on_delete=CASCADE)
    project = models.ForeignKey(to=Project, on_delete=CASCADE)
    permission = models.CharField(max_length=50, choices=CHOICES_PERM)
    role = models.CharField(max_length=20,  choices=CHOICES_ROLES)

    def __str__(self):
        return self.user
