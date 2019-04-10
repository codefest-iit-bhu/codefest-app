from django.urls import path
from .views import *
urlpatterns = [
    path('institutes/',InstituteListView.as_view(),name="college-list"),
    path('events/',EventListView.as_view(),name="event-list"),
    path('profile/',ProfileView.as_view()),
    path('teams/', TeamCreationView.as_view()),
    path('teams/join', TeamJoinView.as_view()),
    path('team/<int:pk>/leave', TeamLeaveView.as_view()),
    # path('teams/'),
]
