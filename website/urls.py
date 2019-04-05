from django.urls import path
from .views import *
urlpatterns = [
    path('institutes/',InstituteListView.as_view(),name="college-list"),
    path('events/',EventListView.as_view(),name="event-list"),
    path('fillprofile/',ProfileView.as_view()),
    path('createteam/', TeamCreationView.as_view()),
    path('jointeam/', TeamJoinView.as_view()),
    path('leaveteam/', TeamLeaveView.as_view()),
]
