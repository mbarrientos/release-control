from django.contrib import admin

from core.models import Release, Project


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    fields = ('commit_id', 'commit_description', 'description', 'project')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
