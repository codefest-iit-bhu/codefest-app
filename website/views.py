from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions,generics,mixins,status
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

class ProfileView(generics.GenericAPIView):
    permission_classes=[]
    serializer_class=ProfileSerializer

    def post(self, request, *args, **kwargs):
        self.request=request
        self.serializer = self.get_serializer(
            data=request.data , context={'request': request}
        )
        self.serializer.is_valid(raise_exception=True)
        self.profile=self.serializer.save(request=request)
        return Response({},status=status.HTTP_200_OK)