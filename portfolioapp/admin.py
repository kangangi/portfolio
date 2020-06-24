from django.contrib import admin
from .models import Profile, Project, Language

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ("languages",)

admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
