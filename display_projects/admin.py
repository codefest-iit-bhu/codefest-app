from django.contrib import admin
from .models import ProjectModel, ProjectRating, ProjectComment

# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(ProjectRating)
admin.site.register(ProjectComment)
