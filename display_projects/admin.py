from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(ProjectRating)
admin.site.register(CommentRating)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentor', 'post','comment', 'created', 'active')
    list_filter = ('active','commentor', 'created', 'updated')
    search_fields = ('commentor', 'post')