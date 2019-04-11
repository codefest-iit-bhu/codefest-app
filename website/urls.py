from django.urls import path
from .views import *
urlpatterns = [
    path('events/',EventListView.as_view(),name="event-list"),
    path('profile/',ProfileView.as_view()),
    path('teams/create/', TeamCreationView.as_view()),
    path('teams/join', TeamJoinView.as_view()),
    path('teams/<int:pk>/', TeamLeaveView.as_view()),
]
