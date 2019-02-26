from django.urls import path
from .views import *
urlpatterns = [
    path('login/', LoginView),
    path('team/',TeamView.as_view(),name="team-cl"),
    path('list-colleges/',InstituteListView.as_view(),name="college-list"),
    path('register/',RegistrationView.as_view(),name="register"),
]
