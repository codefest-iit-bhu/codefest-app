from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins,status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
import json

class EventListView(generics.ListAPIView):
    authentication_classes=[]
    permission_classes=[]
    serializer_class=EventSerializer
    queryset=Event.objects.all()

class ProfileView(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes= [authentication.TokenAuthentication, authentication.SessionAuthentication]
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
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,authentication.SessionAuthentication]
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
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class = TeamJoinSerializer

    def get_queryset(self):
        pass
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        team = self.serializer.save()
        response = TeamDetailSerializer(team)
        return Response(response.data, status = status.HTTP_200_OK)

class TeamLeaveView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    lookup_url_kwarg = 'pk'
    queryset = Team.objects.all()
    
    def perform_destroy(self, instance):
        try:
            member = Membership.objects.get(team = instance, profile  = self.request.user.profile)
        except Membership.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance.leave_team(self.request.user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        self.request = request
        instance = self.get_object()
        return self.perform_destroy(instance)
    
