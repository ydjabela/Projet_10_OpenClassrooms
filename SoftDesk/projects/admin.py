from django.contrib import admin
from projects.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('title', 'description', 'type', 'author_user')


admin.site.register(Project, ProjectAdmin)
