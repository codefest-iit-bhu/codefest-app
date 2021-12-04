from django.urls import path
from .views import *
urlpatterns = [
    path('projects/', Project_list, name="project_list"),
    path('submitproj/', Submit_project, name="submit_project"),
    path('projectdetails/<int:pk>/', Project_detail, name="project_detail"),
    path('project_edit/<int:pk>/', Project_edit, name="project_edit")
]
