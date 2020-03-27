from django.urls import path
from .views import *
urlpatterns = [
    path('events/',EventListView.as_view(),name="event-list"),
    path('profile/',ProfileView.as_view()),
    path('profile/fcm-token/update/', FCMTokenView.as_view()),
    path('teams/create/', TeamCreationView.as_view()),
    path('teams/join/', TeamJoinView.as_view()),
    path('teams/<int:pk>/', TeamLeaveView.as_view()),
    path('teams/<int:pk>/remove/', RemoveFromTeamView.as_view()),
    path('profile/handles/', HandlesView.as_view()),
    path('leaderboard/', LeaderBoardView.as_view()),
    path('resume/',ResumeView.as_view()),
    path('cas/', CALeaderBoardView.as_view()),
]
