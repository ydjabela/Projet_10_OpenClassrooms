from django.contrib import admin
from authentification.models import User


class UsersAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('first_name', 'last_name', 'email', 'password')
# Register your models here.


admin.site.register(User, UsersAdmin)
