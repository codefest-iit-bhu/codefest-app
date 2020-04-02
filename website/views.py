from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins,status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from .serializers import *
from website.permissions import AllowCompleteAndVerified
from .models import *
import json
import logging
logger=logging.getLogger('django')

class EventListView(generics.ListAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes= [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class=EventSerializer
    queryset=Event.objects.all()

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes= [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class=ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        logger.info("[GET Response] : "+str(serializer.data))
        return Response(serializer.data)

    def get_object(self):
        return self.request.user.profile



class TeamCreationView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, AllowCompleteAndVerified]
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
        response = TeamDetailSerializer(team, context=self.get_serializer_context())
        return Response(response.data, status=status.HTTP_200_OK)

class TeamJoinView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, AllowCompleteAndVerified]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class = TeamJoinSerializer

    def get_queryset(self):
        pass
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        team = self.serializer.save()
        response = TeamDetailSerializer(team, context=self.get_serializer_context())
        return Response(response.data, status = status.HTTP_200_OK)

class TeamLeaveView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, AllowCompleteAndVerified]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    lookup_field = 'pk'
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


class RemoveFromTeamView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, AllowCompleteAndVerified]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    lookup_field = 'pk'
    queryset = Team.objects.all()
    serializer_class = RemoveFromTeamSerializer
    

    def get_object(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        return super().get_object()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'team':self.get_object(),
        }
    
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        team= self.serializer.delete()
        response = TeamDetailSerializer(team, context={
            'request':request,
        })
        return Response(response.data, status=status.HTTP_200_OK)

class HandlesView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class = HandleSerializer
    
    def get_queryset(self):
        pass
    def get_object(self):
        return Handles.objects.get_or_create(profile=self.request.user.profile)[0]

class LeaderBoardView(generics.ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset = Profile.objects.exclude(referral_count=0).order_by('-referral_count')[:10]
    serializer_class = LeaderBoardSerializer


@parser_classes([MultiPartParser])
class ResumeView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class = ResumeSerializer
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class CALeaderBoardView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CALeaderboardSerializer
    queryset=CA.objects.order_by('-points')[:15]


class FCMTokenView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    serializer_class = FCMTokenSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def post(self, request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response(status.HTTP_200_OK)