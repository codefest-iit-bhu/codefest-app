from django.urls import path
from .views import *
urlpatterns = [
    path('projects/', Project_list, name="project-list"),
    path('submitproj/', Submit_project, name="submit_project")
]
