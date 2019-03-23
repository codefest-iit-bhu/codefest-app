from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *

class InstituteListView(generics.ListAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=InstituteSerializer
    queryset=Institute.objects.filter(is_active=True)


class EventListView(generics.ListAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=EventSerializer
    queryset=Event.objects.all()
