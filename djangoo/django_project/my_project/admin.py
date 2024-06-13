from django.contrib import admin

from my_project import models

admin.site.register(models.Owner)
admin.site.register(models.Pet)
