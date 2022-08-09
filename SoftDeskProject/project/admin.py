from django.contrib import admin
from project.models import Project, Contributor, Issue, Comment

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('id', 'title', 'description', 'type', 'author_user')


class ContributorAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('id', 'user', 'project', 'permission', 'role')


class IssuesAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('id', 'title', 'desc', 'tag', 'priority', 'project',
                    'status', 'author_user', 'assignee_user', 'created_time')


class CommentAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('id', 'description', 'author_user', 'issue', 'created_time')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssuesAdmin)
admin.site.register(Comment, CommentAdmin)
