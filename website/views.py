from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins,status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
import json

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

class ProfileView(generics.GenericAPIView):
    permission_classes=[]
    serializer_class=ProfileSerializer

    def get_queryset(self):
        pass

    def post(self, request, *args, **kwargs):
        self.request=request
        self.serializer = self.get_serializer(
            data=request.data , context={'request': request}
        )
        self.serializer.is_valid(raise_exception=True)
        self.profile=self.serializer.save(request=request)
        return Response({},status=status.HTTP_200_OK)

class TeamCreationView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = TeamCreationSerializer

    def get_queryset(self):
        pass
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(
            data=request.data
        )
        self.serializer.is_valid(raise_exception=True)
        team = self.serializer.save()
        response = TeamDetailSerializer(team)
        return Response(response.data, status=status.HTTP_200_OK)

class TeamJoinView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = TeamJoinSerializer

    def get_queryset(self):
        pass
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        team = seld.serializer.save()
        response = TeamDetailSerializer(team)
        return Response(response.data, status = status.HTTP_200_OK)

class TeamLeaveView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = TeamLeaveSerializer

    def get_queryset(self):
        pass
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        (team, num_members) = self.serializer.save()
        if num_members ==0:
            return Response({}, status=status.HTTP_200_OK)
        response = TeamDetailSerializer(team)
        return Response(response.data, status = status.HTTP_200_OK)