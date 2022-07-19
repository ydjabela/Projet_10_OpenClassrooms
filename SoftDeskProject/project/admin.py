from django.contrib import admin
from project.models import Project, Contributor, Issue, Comment

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('title', 'description', 'type', 'author_user')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
