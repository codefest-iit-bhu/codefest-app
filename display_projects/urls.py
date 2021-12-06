from django.urls import path
from .views import *
urlpatterns = [
    path('projects/', Project_list, name="project_list"),
    path('submitproj/', Submit_project, name="submit_project"),
    # path('projectdetails/<int:pk>/', Project_detail, name="project_detail"),
    path('project_edit/<int:pk>/', Project_edit, name="project_edit"),
    path('project_like/<int:pk>/', Project_Like, name="project_like"),
    path('comment_like/<int:pk>/', Comment_Like, name="comment_like"),
    path('comment_del/<int:pk>/', Comment_Del, name="comment_del"),
    path('project_view/<int:pk>/', Project_View, name="project_view"),
    path('project_delete/<int:pk>/', Project_delete, name="project_delete"),
]
