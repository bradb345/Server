from django.contrib import admin
from .models import Project, Comment, Project_type

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Project_type)
